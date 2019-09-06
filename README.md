# BayesianFramework
> A framework for Bayesian model selection (BMS) and Bayesian model Averaging (BMA).  

A framework to implement Bayesian model selection and model averaging scheme to linear regression models. It can be used to identify the best model amongst several competing linear regression models. Furthermore, when the model uncertainty is high, it can be used to perform Bayesian model averaging to make reliable and robust estimation of the quantities of interest.

## Installing / Getting started

To use this package, you need the following packages:

```shell
numpy>=1.12
sklearn
matplotlib>=3.1
pandas>=0.25.1
```

After you have all the required dependency, you can download the code from github using:

```shell
git clone https://github.com/mamunm/BayesianFramework
```

Then, you can run `setup.py` to install:

```shell
python setup.py install 
```

Alternatively, you can add the file location to your `PYTHONPATH`:

```shell
export PYTHONPATH="/path/to/BayesianFramework:${PYTHONPATH}"
```


## Features

What's all the bells and whistles this project can perform?
* linreg: performs linear regression on data
* linzoo: constructs the linear regression zoo from the dataframe
* bayesframe: performs Bayesian model selction and averaging and can be used to make future prediction.

## How to use it:

### LinReg

Here, I demonstrate a simple code snippet to show how to use `bayesframe.LinReg` on any data:

```python
#import module
from bayesframe import LinReg
from sklearn.datasets import load_boston

#get the data
data = load_boston()
X = data['data'][:, 1]
y = data['target']

# Initialize the model 
lin = LinReg(X=X, y=y, val_scheme="leave_one_out")

#print model data
print(lin.get_model_data()) 
```
Running this script will produce the following output:

```shell
print(lin.get_model_data())
{'slope': array([0.14213999]), 'intercept': 20.917579117799832, 'rmse': 8.60490557714858, 'n_dp': 506}
```

Here, the `slope` and `intercept` are the model parameters, `n_dp` is the number of data points used to fit the model, and `rmse` is the model's root mean squred error. If `val_scheme` is used `None` or default, it will compute the sample variance. To approximate the population variance, you can use `leave_one_out` or `k-Fold` cross validation scheme. In the `k-Fold` scheme, you need to give an integer for the value of `k`, e.g., for 5 fold cv, use `5-Fold`. 

### LinZoo

Now, we show a simple demonstration of the `bayesframe.linzoo.LinZoo` function:

```python
#import module
from bayesframe import load_data
from bayesframe import LinZoo

#get the data
data = load_data()

#Initialize the model
```

### BayesFrame




