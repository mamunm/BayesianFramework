import numpy as np
import pandas as pd
from linreg import LinReg
from itertools import combinations
import matplotlib.pyplot as plt

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
                des_comb = list(comb)
                X, y = self.get_data(des_comb)
                if len(y.shape) == 2:
                    y =y.reshape(-1)
                lin = LinReg(X=X, y=y, val_scheme=self.val_scheme)
                self.zoo['_'.join(des_comb)] = lin.get_model_data()
       
        rmse_min = min([value['rmse'] for value in self.zoo.values()])
        for key, value in self.zoo.items():
            rmse = value['rmse']
            n = value['n_dp']
            k = len(value['slope']) + 1
            bic = n * np.log((rmse/rmse_min)**2) + k * np.log(n)
            
            if self.bic_scheme == 'per_n':
                self.zoo[key]['BIC'] = bic / n
            else:
                self.zoo[key]['BIC'] = bic
        
        bic_min = min([value['BIC'] for value in self.zoo.values()])
        for key, value in self.zoo.items():
            self.zoo[key]['Delta_BIC'] = value['BIC'] - bic_min
    
    def get_data(self, comb):
        df = self.df[comb + self.target]
        df = df.dropna()
        return df[comb].to_numpy(), df[self.target].to_numpy()

    def plot_envelope(self):
        plt.figure(facecolor='white')
        plt.style.use('classic')
        plt.grid(color='grey', linewidth=0.5, linestyle='--')
        plt.xlabel("# of descriptors", fontsize=14)
        plt.ylabel("BIC", fontsize=14)
        data = [(len(v['slope'])+1, v['BIC']) for v in self.zoo.values()]
        plt.scatter(*zip(*data), color="green", s=40)
        min_data = []
        for ndes in range(2, len(self.descriptors) + 2):
            min_data.append(min([i for i in data if i[0]==ndes], 
                    key=lambda x: x[1]))
        plt.plot(*zip(*min_data), color="blue", linewidth=3)
        min_min_data = min(min_data, key=lambda x: x[1])
        plt.xticks([i[0] for i in min_data])
        plt.scatter(min_min_data[0], min_min_data[1],
                color='red', marker='*', s=500)
        plt.tight_layout()
        return plt



