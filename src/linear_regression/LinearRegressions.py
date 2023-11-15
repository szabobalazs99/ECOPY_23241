import pandas as pd
import statsmodels.api as sm
import numpy as np
from scipy.stats import t, f
from typing import List, Union


class LinearRegressionSM:
    def __init__(self, left_hand_side, right_hand_side):
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side
        self._model = None

    def fit(self):
        X = sm.add_constant(self.right_hand_side)
        y = self.left_hand_side
        model = sm.OLS(y, X).fit()
        self._model = model

    def get_params(self):
        if self._model is not None:
            beta_coefficients = self._model.params
            return pd.Series(beta_coefficients, name='Beta coefficients')
        else:
            return None

    def get_pvalues(self):
        if self._model is not None:
            p_values = self._model.pvalues
            return pd.Series(p_values, name='P-values for the corresponding coefficients')
        else:
            return None

    def get_wald_test_result(self, restrictions):
        if self._model is not None:
            wald_test = self._model.wald_test(restrictions)
            f_value = format(float(wald_test.statistic), '.2f')
            p_value = format(float(wald_test.pvalue), '.3f')
            return f'F-value: {f_value}, p-value: {p_value}'
        else:
            return None

    def get_model_goodness_values(self):
        if self._model is not None:
            ars = format(self._model.rsquared_adj, '.3f')
            ak = format(self._model.aic, '.2e')
            by = format(self._model.bic, '.2e')
            return f'Adjusted R-squared: {ars}, Akaike IC: {ak}, Bayes IC: {by}'
        else:
            return None


class LinearRegressionNP:
    def __init__(self, left_hand_side, right_hand_side):
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side
        self._model = None

    def fit(self):
        X = np.column_stack((np.ones(len(self.right_hand_side)), self.right_hand_side))
        y = self.left_hand_side
        beta = np.linalg.inv(X.T @ X) @ X.T @ y
        self.beta = beta

    def get_params(self):
        return pd.Series(self.beta, name='Beta coefficients')

    def get_pvalues(self):
        X = np.column_stack((np.ones(len(self.right_hand_side)), self.right_hand_side))
        y = self.left_hand_side
        n, k = X.shape
        beta = self.beta
        H = X @ np.linalg.inv(X.T @ X) @ X.T
        residuals = y - X @ beta
        residual_variance = (residuals @ residuals) / (n - k)
        standard_errors = np.sqrt(np.diagonal(residual_variance * np.linalg.inv(X.T @ X)))
        t_statistics = beta / standard_errors
        df = n - k
        p_values = [2 * (1 - t.cdf(abs(t_stat), df)) for t_stat in t_statistics]
        p_values = pd.Series(p_values, name="P-values for the corresponding coefficients")
        return p_values

    def get_wald_test_result(self, R):
        X = np.column_stack((np.ones(len(self.right_hand_side)), self.right_hand_side))
        y = self.left_hand_side
        beta = self.beta
        residuals = y - X @ beta
        r_matrix = np.array(R)
        r = r_matrix @ beta
        n = len(self.left_hand_side)
        m, k = r_matrix.shape
        sigma_squared = np.sum(residuals ** 2) / (n - k)
        H = r_matrix @ np.linalg.inv(X.T @ X) @ r_matrix.T
        wald = (r.T @ np.linalg.inv(H) @ r) / (m * sigma_squared)
        p_value = 1 - f.cdf(wald, dfn=m, dfd=n - k)
        return f'Wald: {wald:.3f}, p-value: {p_value:.3f}'

    def get_model_goodness_values(self):
        X = np.column_stack((np.ones(len(self.right_hand_side)), self.right_hand_side))
        y = self.left_hand_side
        n, k = X.shape
        beta = self.beta
        y_pred = X @ beta
        ssr = np.sum((y_pred - np.mean(y)) ** 2)
        sst = np.sum((y - np.mean(y)) ** 2)
        centered_r_squared = ssr / sst
        adjusted_r_squared = 1 - (1 - centered_r_squared) * (n - 1) / (n - k)
        result = f"Centered R-squared: {centered_r_squared:.3f}, Adjusted R-squared: {adjusted_r_squared:.3f}"
        return result


class LinearRegressionGLS:
    def __init__(self, left_hand_side: pd.DataFrame, right_hand_side: pd.DataFrame):
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side

    def fit(self):
        X = np.column_stack((np.ones(len(self.right_hand_side)), self.right_hand_side))
        self.X = X
        beta_hat = np.linalg.inv(X.T @ X) @ X.T @ self.left_hand_side
        residuals = self.left_hand_side - X @ beta_hat
        squared_residuals = residuals ** 2
        self.squared_residuals = squared_residuals
        V_inv = np.diag(1 / np.sqrt(squared_residuals))
        self.V_inv = V_inv
        self.beta_hat_gls = np.linalg.inv(X.T @ V_inv @ X) @ X.T @ V_inv @ self.left_hand_side

    def get_params(self):
        beta_names = [f'Beta_{i}' for i in range(len(self.beta_hat_gls))]
        return pd.Series(self.beta_hat_gls, index=beta_names, name='Beta coefficients')

    def get_pvalues(self):
        dof = len(self.right_hand_side) - len(self.beta_hat_gls)
        t_values = self.beta_hat_gls / np.sqrt(np.diag(np.linalg.inv(self.X.T @ self.V_inv @ self.X)) * (np.sum((self.X - self.X.mean(axis=0)) ** 2, axis=0) / dof))
        p_values = [2 * min(t.cdf(-np.abs(t_val), dof), t.cdf(np.abs(t_val), dof)) for t_val in t_values]
        return pd.Series(p_values, index=[f'P-value_{i}' for i in range(len(self.beta_hat_gls))], name='P-values for the corresponding coefficients')

    def get_wald_test_result(self, R: List[List[float]]):
        num_constraints = len(R)
        q = len(self.right_hand_side) - len(self.beta_hat_gls)
        F_value = ((np.array(R) @ self.beta_hat_gls).T @ np.linalg.inv(np.array(R) @ np.linalg.inv(self.X.T @ self.V_inv @ self.X) @ np.array(R).T) @ (np.array(R) @ self.beta_hat_gls)) / num_constraints
        p_value = 1 - f.cdf(F_value, num_constraints, q)
        return f'Wald: {F_value:.3f}, p-value: {p_value:.3f}'

    def get_model_goodness_values(self):
        SSR = np.sum((np.log(self.squared_residuals) - np.mean(np.log(self.squared_residuals))) ** 2)
        SST = np.sum((np.log(self.squared_residuals) - np.mean(np.log(self.left_hand_side))) ** 2)
        R_squared = SSR / SST
        adj_R_squared = 1 - (1 - R_squared) * ((len(self.left_hand_side) - 1) / (len(self.left_hand_side) - len(self.beta_hat_gls) - 1))
        return f'Centered R-squared: {R_squared:.3f}, Adjusted R-squared: {adj_R_squared:.3f}'