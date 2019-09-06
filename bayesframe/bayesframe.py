import numpy as np
from .linzoo import LinZoo
import pandas as pd
from sklearn.metrics import mean_squared_error

class BayesFrame:
    """A Bayesian model selection and averaging performer."""

    def __init__(self,
                 fpath=None,
                 target=None,
                 val_scheme=None,
                 bic_scheme=None,
                 model_scheme=['selection']):
        
        lin = LinZoo(fpath=fpath, target=target, 
                     val_scheme=val_scheme, bic_scheme=bic_scheme)
        lin.build_zoo()
        self.zoo = lin.zoo
        del lin
        self.best_model = min(self.zoo.keys(), key=lambda x:self.zoo[x]['BIC'])
        self.model_scheme = model_scheme[0]
        if self.model_scheme == "selection":
            self.zoo = {self.best_model: self.zoo[self.best_model]}
        if self.model_scheme == 'averaging':
            ratio = model_scheme[1]
            best_bic = self.zoo[self.best_model]['BIC'] 
            if ratio != 'all':
                self.zoo = {k: v for k, v in self.zoo.items() 
                            if v['BIC'] < best_bic + abs(best_bic) * ratio}

    def get_Epred(self, D):
        if self.model_scheme == "selection":
            slope = self.zoo[self.best_model]['slope']
            intercept = self.zoo[self.best_model]['intercept']
            des = self.best_model.split('_')
            return intercept + sum(m*D[n] for m, n in zip(slope, des))

        if self.model_scheme == "averaging":
            E_Bic = []
            for k, v in self.zoo.items():
                slope = v['slope']
                intercept = v['intercept']
                des = k.split('_')
                E_Bic += [(intercept + sum(m*D[n] for m, n in zip(slope, des)),
                    v['Delta_BIC'])]
            return self.get_bma(E_Bic)

    def get_bma(self, E):
        Delta_BIC = np.array([i[1] for i in E])
        E = np.array([i[0] for i in E])
        ExDBIC = np.exp(-Delta_BIC/2)
        return np.sum(ExDBIC * E) / np.sum(ExDBIC)

    def __call__(self, fpath=None, data=None, outpath=None, print_rmse=True):
        if fpath:
            data = pd.read_csv(fpath, encoding="utf-8").to_dict(orient="records")
        else:
            data = data
        for d in data:
            d['Epred'] = self.get_Epred(d)
        out_df = pd.DataFrame(data)
        if outpath:
            out_df.to_csv(fpath)
        else:
            out_df.to_csv(outpath)
        
        if print_rmse:
            Epr = out_df['Epred'].to_numpy()
            Etr = out_df['Target'].to_numpy()
            print('Computed RMSE: {}'.format(np.sqrt(
                mean_squared_error(Epr, Etr))))

            
