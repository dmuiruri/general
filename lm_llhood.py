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
    
    The log pdf of normal where x is the result of the func which is
    the error term (€) here. So we get the log-likelihood of the x in
    the normal distribution.
    """
    return np.sum(-0.5*np.log(2*np.pi)-0.5*(y - coefs[1] - coefs[0]*x)**2)

