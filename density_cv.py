#! /usr/bin/env python

"""
Implementation of Density Estimation and Cross Validation

Density estimation: Given a sample drawn from a probability
distribution, how can we represent that distribution as a continuous
probability distribution.

Kernels: Gaussian Kernel, Uniform Kernel, Epanechnikov Kernel

Kernel Density Estimate: A formular that make use of a given kernel to
estimate the kernel density of a given point
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

    x: input array containing obs to be estimated
    h: width of the kernel
    """
    y = np.zeros(len(t))
    for i in range(len(t)):
        y[i] = np.mean(K_gauss((t[i] - x)/h))/h
    return y

if __name__ == '__main__':
    t = np.linspace(-2, 10, 100)
    nb = plt.hist(d, 30, normed=True)

    plt.plot(t, kernel_density(t, d, 3.0), label='h=3.0')
    plt.plot(t, kernel_density(t, d, 1.0), label='h=1.0')
    plt.plot(t, kernel_density(t, d, 0.3), label='h=0.3')
    plt.plot(t, kernel_density(t, d, 0.1), label='h=0.1')
    plt.show()
    
