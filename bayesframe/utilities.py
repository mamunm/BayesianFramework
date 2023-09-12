import os
import pandas as pd
import bayesframe

def load_data():
    path = '/'.join(bayesframe.__path__[0].split('/')[:-1]) 
    path += '/data/data.csv'
    if not os.path.isfile(path):
        print("Could not find data file locally. Will download.")
        path = "https://raw.githubusercontent.com/mamunm/BayesianFramework/master/data/data.csv"
    return pd.read_csv(path)

def load_test_data():
    path = '/'.join(bayesframe.__path__[0].split('/')[:-1])  
    path += '/data/data_test.csv'
    if not os.path.isfile(path):
        print("Could not find test_data file locally. Will download.")
        path = "https://raw.githubusercontent.com/mamunm/BayesianFramework/master/data/data_test.csv"
    return pd.read_csv(path)