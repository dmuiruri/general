#! /usr/bin/env python

"""
A module that demonstrates the use of log likelihood towards the
estimation of linear regression and robust regression. When estimating
the likelihood, we are estimating for the parameters of the model.

The maximum log-likelihood implementation below gets the maximum by
MINIMISING the NEGATIVE log-likelihood

A typical linear regression assumes that the estimation errors follow
a Normal distribution, however, a robust regression can be obtained by
using an alternative distribution of the error terms.

The Likelihood of a variable in a given distribution => pdf of that given variable
The log-likelihood of a variable in a given distn => log pdf version of the given dist


"""
import matplotlib.pyplot as plt
import autograd.numpy as np
import autograd
from scipy.optimize import minimize
from scipy.stats import norm

def linear_reg_normlogpdf(coefs, x, y):
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
    func = lambda c: -linear_reg_normlogpdf(c, np.array(x), np.array(y))
    d_func = autograd.grad(func) # gradient func
    v = minimize(func, np.ones(2), jac=d_func, method='L-BFGS-B')
    return v

def linear_reg_laplacelogpdf(coefs, x, y):
    """
    Create laplace model to estimate the distribution of the error
    term of a linear regression model
    """
    return np.sum(-np.log(2)-np.abs(y - coefs[1] - coefs[0]*x))

def laplace_regression(x, y):
    """
    Optimize the error function to obtain maximum likelihood of the
    parameters (const and Beta_1)
    """
    func = lambda c: -linear_reg_laplacelogpdf(c, np.array(x), np.array(y))
    d_func = autograd.grad(func)
    v = minimize(func, np.ones(2), jac=d_func, method='L-BFGS-B')
    return v


if __name__ == '__main__':
    # Compare a regular linear regression which assumes the errors
    # follow a Normal distrubution to a robust regression where the
    # errors are modelled as to follow laplace distribution.
    x = np.arange(10)
    y = np.copy(x); y[8]=0

    v_norm = linear_regression(x, y)
    print("Normal lr:", v_norm)
    v_lap = laplace_regression(x, y)
    print("Laplace lr:", v_lap)

    # Plot
    t = np.array([0, 10])
    plt.plot(x, y, '*')
    plt.plot(t, v_norm.x[0]*t + v_norm.x[1], label='norm_lr')
    plt.plot(t, v_lap.x[0]*t + v_lap.x[1], label='lap_lr')
    plt.legend()
    plt.show()
