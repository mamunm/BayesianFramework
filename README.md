# BayesianFramework
> A framework for Bayesian model selection (BMS) and Bayesian model Averaging (BMA).  

A framework to implement Bayesian model selection and model averaging scheme to linear regression models. It can be used to identify the best model amongst several competing linear regression models. Furthermore, when the model uncertainty is high, it can be used to perform Bayesian model averaging to make reliable and robust estimation of the quantities of interest.

## Installing / Getting started

To use this package, you need the following packages:

```shell
numpy>=1.12
sklearn
matplotlib>=3.1
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

## Configuration

Here you should write what are all of the configurations a user can enter when
using the project.

## How to use it:

### LinReg

### LinZoo

### BayesFrame




