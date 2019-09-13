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

    
