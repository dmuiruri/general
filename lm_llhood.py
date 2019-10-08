#! /usr/bin/env python

"""
A module that demonstrates the use of maximum likelihood towards the
estimation of linear regression and robust regression

The Likelihood of a variable in a given distribution => pdf of that given variable
The log-likelihood of a variable in a given distn => log pdf version of the given dist


"""
import numpy as np
import autograd
from scipy.optimize import minimize
from scipy.stats import norm

def linear_reg_logl(coefs, x, y):
    """
    Log likelihood for a linear regression where the error term
    follows a normal distribution see the normal dist pdf with mu=0
    std=1 in log
    
    The logpdf of normal distribution where x is the result of the
    func which being optimized in this case the error term (€). So we
    get the log-likelihood of the x in the normal distribution.

    Note: For some reason usint scipy.stats.norm.logpdf(x) does not
    work with autograd.
    """
    return np.sum(-0.5*np.log(2*np.pi)-0.5*(y - coefs[1] - coefs[0]*x)**2)


def linear_regression(x, y):
    """
    Estimate the linear regression coefficients using maximum
    likelihood estimation

    Setup the function to be optimized, which is the logpdf of the
    errors (€), the gradient of the function, which is setup by using
    autograd which performs gradient computations.
    """
    func = lambda c: -linear_reg_logl(c, np.array(x), np.array(y))
    d_func = autograd.grad(func) # gradient func
    v = minimize(func, np.ones(2), jac=d_func, method='L-BFGS-B')
    return v


if __name__ == '__main__':
    x = np.arange(10)
    y = np.copy(x); y[8]=0

    v_norm = linear_regression(x, y)
    print(v_norm)
