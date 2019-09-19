#! /usr/bin/env python

"""
An of the implementation a Markov Chain Monte Carlo algorithm,
particularly this implementation follows the Metropolis-Hastings
Algorithm.

When performing MCMC, some parameters need to be tuned otherwise the
chain may take long to converge. When the plotted chaon looks like a
random walk, it means that the chain has not converged.
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
    drawproposal: proposal distribution function 
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

if __name__ == '__main__':
    np.random.seed(42)
    thetas = mcmc_mh_sampler(0.0, 1000,
                             lambda theta: np.rando,normal(theta),
                             lambda theta: np.random.uniform(theta-0.5, theta+0.5))
    fig, ax = plt.subplots(1, 3)
    # plottig the true density
    fit = norm.pdf(thetas, np.mean(thetas), np.std(thetas))
    ax[0].hist(thetas, 50, normed=True, alpha=0.4)
    ax[0].plot(thetas, fit, label='True density')

    # plotting the trace plot
    thetas = thetas[len(thetas)//2:] # first half of the samples are discarded
    ax[1].plot(thetas[::10]) # plot the thinned(every 10th sample) samples
    ax[2].hist(thetas[::10]), 50, normed=True)
    plt.show()
