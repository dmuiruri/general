#! /usr/bin/env python

"""
An of the implementation a Markov Chain Monte Carlo algorithm,
particularly this implementation follows the Metropolis-Hastings
Algorithm.
"""

import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
from scipy.stats import norm

def mcmc_mh_sampler(theta0, n, logtarget, drawproposal):
    """
    Generate Markov Chain.

    Implements the Metropolic-Hastings Sampler
    theta0: Initial State
    n: No. of states
    logtarget: target function
    drawproposa: proposal distribution function 
    """
    theta = theta0
    thetas = np.zeros(n)
    accepted = 0
    for i in range(n):
        theta_prop = drawproposal(theta)
        if np.log(np.random.rand()) < logtarget(theta_prop) - logtarget(theta):
            theta = theta_prop
            accepted += 1
        thetas[i] = theta
    print("Acceptance Rate: ", accepted/n)
    return thetas



