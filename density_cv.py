#! /usr/bin/env python

"""
Implementation of Density Estimation and Cross Validation

Density estimation: Given a sample drawn from a probability
distribution, how can we represent that distribution as a continuous
probability distribution.

Kernels: Gaussian Kernel, Uniform Kernel, Epanechnikov Kernel

Kernel Density Estimate: A formular that make use of a given kernel to
estimate the kernel density of a given point

Observations: When "h" is too large in the case of a guassian kernel,
the plot is very thick, on the contrast, when "h" is too small, the
density line becomes too jagged.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

d = pd.read_csv('http://www.cs.helsinki.fi/u/ahonkela/teaching/compstats1/toydata.txt').values

def K_gauss(x):
    """
    Generate the Gaussian Kernel for x
    """
    return (np.exp((-x**2)/2))/(np.sqrt(2*np.pi))

def K_uniform(x):
    """ 
    Compute the uniform Kernel 
    """
    return 0.5 * (np.abs(x) < 1) 

def K_epanechnikov(x):
    """
    Compute the Epanechnikov kernel
    """
    return (3 / 4)*(1 - x**2)*(np.abs(x) < 1) 

def kernel_density(t, x, h):
    """
    Calculate the kernel density

    t: plot points
    x: input array containing obs to be estimated
    h: width of the kernel
    """
    y = np.zeros(len(t))
    for i in range(len(t)):
        y[i] = np.mean(K_gauss((t[i] - x)/h))/h
    return y

def true_density_comparison():
    """
    If the samples were from a known distrubution, for example the
    normal distrubution, we could plot the real density and observe
    the difference.
    """
    x = np.sort(np.random.normal(0, 1, 1000))
    t = np.linspace(np.min(x), np.max(x), 100)
    nb = plt.hist(x, 30, normed=True)
    fit = norm.pdf(x, np.mean(x), np.std(x))
    plt.plot(x, fit, label='True Density')
    plt.plot(t, kernel_density(t, x, 1.0), label='h=1.0')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    true_density_comparison()
#     t = np.linspace(-2, 10, 100)
#     nb = plt.hist(d, 30, normed=True)

#     plt.plot(t, kernel_density(t, d, 3.0), label='h=3.0')
#     plt.plot(t, kernel_density(t, d, 1.0), label='h=1.0')
#     plt.plot(t, kernel_density(t, d, 0.3), label='h=0.3')
#     plt.plot(t, kernel_density(t, d, 0.1), label='h=0.1')
#     plt.legend()
#     plt.show()
    
