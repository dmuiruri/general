#! /usr/bin/env python

import numpy as np
import pandas as pd

"""
Numeric computation/algorithms

This module contains various implementations of the variance algorithm
as a way to demonstrate potential challenges of numeric computation,
particularly integer overflow.

How can variance be computed in a stable form?
"""

def twopass_var(x):
    """
    Calculate the variance using a single pass
    """
    x = np.array(x)
    x_mean = np.mean(x)
    return (1/len(x)-1) * sum([(i-x_mean)**2 for i in x])

if __name__ == '__main__':
    mu = 10e9
    sigma = 1
    samples = 1000
    x = np.random.normal(mu, sigma, samples)
    print("Var of vector x using np {}".format(np.var(x)))
    print("Var of vector x using two pass algorithm: {}".format(singlepass_var(x)))
