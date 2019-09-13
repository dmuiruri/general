#!  /usr/bin/env python

"""
Permutation testing is a mechanism to evaluate the distribution of a
test statistic under the Null Hypothesis based on Simulation

In this exercise the permutation testing is used to determine whether
the ages of male and female participants in a data set are
statistically different using the absolute different of the means as
the test statistic.
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_csv('http://www.cs.helsinki.fi/u/ahonkela/teaching/compstats1/fram.txt', sep='\t')
Nperms = 1000 # No of permutations

def pvalue(var='AGE'):
    """
    Calculate the p-value based on simulated means

    var: variable on which to test difference of means
    s1: series
    s2: series
    """
    s1 = data[var][data['SEX'] == 'male']
    s2 = data[var][data['SEX'] == 'female']

    truediff = np.abs(np.mean(s1) - np.mean(s2))
    meandiffs = np.zeros(Nperms)
    print("=== Evaluating difference statistical significance of means on: ", var)
    print("True mean difference {}".format(truediff))
    print("Means: ", np.mean(s1), np.mean(s2))
    
    n = len(s1)
    for i in range(Nperms):
        s3 = np.random.permutation(s1.append(s2))
        meandiffs[i] = np.abs(np.mean(s3[0:n]) - np.mean(s3[n:]))
    return (np.sum(truediff <= meandiffs) + 1)/(len(meandiffs) + 1)

if __name__ == '__main__':
    print("P-Value: ", pvalue())
    print("P-Value: ", pvalue(var='CHOL'))
    print("P-Value: ", pvalue(var='SBP'))
    print("P-Value: ", pvalue(var='FRW'))
    print("P-Value: ", pvalue(var='DBP'))
