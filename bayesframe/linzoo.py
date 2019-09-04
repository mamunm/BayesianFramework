import numpy as np
import pandas as pd
from linreg import LinReg
from itertools import combinations

class LinZoo:
    """An object to build the linear regression zoo from a given dataframe"""

    def __init__(self, 
                 fpath=None, 
                 target=None,
                 val_scheme=None,
                 bic_scheme='per_n'):
        self.df = pd.read_csv(fpath, encoding="utf-8")
        self.target = [target]
        self.val_scheme = val_scheme
        self.bic_scheme = bic_scheme
        self.descriptors = list([i for i in self.df.columns 
            if i != target])

    def build_zoo(self):
        self.zoo = {}
        for ndes in range(1, len(self.descriptors) + 1):
            for comb in combinations(self.descriptors, ndes):
                X, y = self.get_data(list(comb))
                lin = LinReg(X=X, y=y, val_scheme=self.val_scheme)
                self.zoo['_'.join(sorted(comb))] = lin.get_model_data()
       
        rmse_min = min([value['rmse'] for value in self.zoo.values()])
        for key, value in self.zoo.items():
            rmse = value['rmse']
            n = value['n_dp']
            k = len(value['slope']) + 1
            bic = n * np.log((rmse/rmse_min)**2) + k * np.log(n)
            
            if self.bic_scheme == 'per_n':
                self.zoo[key]['bic'] = bic / n
            else:
                self.zoo[key]['bic'] = bic
        
        bic_min = min([value['bic'] for value in self.zoo.values()])
        for key, value in self.zoo.items():
            self.zoo[key]['Delta_Bic'] = value['bic'] - bic_min
    
    def get_data(self, comb):
        df = self.df[comb + self.target]
        df = df.dropna()
        return df[comb].to_numpy(), df[self.target].to_numpy()



