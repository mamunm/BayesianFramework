import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import KFold

class LinReg:
    """Linear Regression Performer.

    A class to perform linear regression analysis on data.
    """

    def __init__(self, X=None, y=None, val_scheme=None):
        self.X = np.array(X)
        self.y = np.array(y)
        if len(self.X.shape) == 1:
            self.X = self.X.reshape(-1, 1)
        self.val_scheme = val_scheme
        self.lr = LinearRegression().fit(self.X, self.y)
    
    def get_RMSE_oos(self, X, y):
        return np.sqrt(mean_squared_error(self.lr.predict(X), y))

    def get_model_data(self):
        return {'slope': self.lr.coef_,
                'intercept': self.lr.intercept_,
                'rmse': self.compute_RMSE(),
                'n_dp': len(self.y)}

    def predict(self, X):
        return self.lr.predict(X)
    
    def compute_RMSE(self):
        if self.val_scheme is None:
            return np.sqrt(mean_squared_error(self.lr.predict(self.X), self.y))
        else:
            if self.val_scheme == 'leave_one_out':
                locv = LeaveOneOut()
            elif 'Fold' in self.val_scheme:
                k = int(self.val_scheme.split('-')[0])
                locv = KFold(n_splits=k)
            else:
                msg = 'Invalid value encountered for validation scheme.'
                raise ValueError(msg)

            y_true = []
            y_pred = []
            for tr_id, ts_id in locv.split(self.y):
                XTR, XTS, YTR = self.X[tr_id], self.X[ts_id], self.y[tr_id]
                y_true.extend(self.y[ts_id])
                y_pred.extend(LinearRegression().fit(XTR, YTR).predict(XTS))
            return np.sqrt(mean_squared_error(y_true, y_pred))
    

