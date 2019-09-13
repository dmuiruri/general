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
male = data['DBP'][data['SEX'] == 'male']
female = data['DBP'][data['SEX'] == 'female']

def pvalue(s1, s2):
    """
    Calculate the p-value based on simulated means
    """
    truediff = np.abs(np.mean(s1) - np.mean(s2))
    meandiffs = np.zeros(Nperms)
    print("True mean difference {}".format(truediff))
    print("Means: ", np.mean(s1), np.mean(s2))
    
    n = len(s1)
    for i in range(Nperms):
        s3 = np.random.permutation(s1.append(s2))
        meandiffs[i] = np.abs(np.mean(s3[0:n]) - np.mean(s3[n:]))
    return (np.sum(truediff <= meandiffs) + 1)/(len(meandiffs) + 1)

if __name__ == '__main__':
    print("P-Value: ", pvalue(male, female))
