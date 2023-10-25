import pandas as pd
import statsmodels.api as sm


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




