import pandas as pd
import statsmodels.api as sm
import numpy as np
from scipy.stats import t, f
from typing import List


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
    def __init__(self, left_hand_side: pd.DataFrame, right_hand_side: pd.DataFrame):
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side
        self._model = None

    def fit(self):
        X = self.right_hand_side
        X = pd.concat([pd.Series(1, index=X.index, name='Intercept'), X], axis=1)
        y = self.left_hand_side
        beta = np.linalg.inv(X.T @ X) @ X.T @ y
        residuals = y - X @ beta
        residual_variance = np.var(residuals, ddof=X.shape[1])
        total_variance = np.var(y, ddof=X.shape[0])
        rsquared = 1 - residuals.var() / total_variance
        n = X.shape[0]
        k = X.shape[1] - 1
        adjusted_rsquared = 1 - (1 - rsquared) * (n - 1) / (n - k - 1)
        self._model = {
            'coefficients': beta,
            'residuals': residuals,
            'rsquared': rsquared,
            'adjusted_rsquared': adjusted_rsquared,
            'residual_variance': residual_variance
        }

    def get_params(self):
        if self._model is not None:
            beta_coefficients = self._model['coefficients']
            return pd.Series(beta_coefficients, name='Beta coefficients')
        else:
            return None

    def get_pvalues(self):
        if self._model is not None:
            residuals = self._model['residuals']
            residual_variance = self._model['residual_variance']
            X = self.right_hand_side
            X = pd.concat([pd.Series(1, index=X.index, name='Intercept'), X], axis=1)
            n = X.shape[0]
            k = X.shape[1] - 1
            sse = residuals.T @ residuals
            standard_errors = np.sqrt(np.diag(sse * np.linalg.inv(X.T @ X) * residual_variance))
            t_statistic = self._model['coefficients'] / standard_errors
            p_values = 2 * (1 - t.cdf(np.abs(t_statistic), df=n - k - 1))
            p_values = pd.Series(np.minimum(p_values, 1 - p_values) * 2, name='P-values for the corresponding coefficients')
            return p_values
        else:
            return None

    def get_wald_test_result(self, R: List[List[float]]):
        if self._model is not None:
            beta = self._model['coefficients']
            n = self.right_hand_side.shape[0]
            k = self.right_hand_side.shape[1]
            df_R = len(R)
            df_E = n - k
            r = np.array(R)
            wald_value = (r @ beta) @ np.linalg.inv(r @ np.linalg.inv(self._model['residual_variance'] * np.eye(n - k)) @ r.T)
            p_value = 1 - f.cdf(wald_value, df_R, df_E)
            result = f"Wald: {wald_value:.3f}, p-value: {p_value:.3f}"
            return result
        else:
            return None

    def get_model_goodness_values(self):
        if self._model is not None:
            rsquared = self._model['rsquared']
            adjusted_rsquared = self._model['adjusted_rsquared']
            result = f"Centered R-squared: {rsquared:.3f}, Adjusted R-squared: {adjusted_rsquared:.3f}"
            return result
        else:
            return None



