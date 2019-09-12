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

print(data.columns)

Nperms = 1000 # No of permutations

m_mean_age = np.mean(data['AGE'][data['SEX'] == 'male'])
f_mean_age = np.mean(data['AGE'][data['SEX'] == 'female'])

true_m_diff = m_mean_age - f_mean_age

meandiffs = np.zeros(Nperms)

print("True mean difference {}".format(true_m_diff))

def permute_arrays(s1, s2):
    """
    permute two series
    
    A helper function to permute/shuffle two series
    """
    n = len(s1)
    s3 = np.random.permutation(s1.append(s2))
    return s3[0:n], s3[n:]
    
def permutation_test(x1, x2):
    """
    Run permutations
    """
    for i in range(Nperms):
        s1, s2 = permute_arrays()
        meandiffs[i] = np.abs(np.mean(s1) - np.mean(s2))

def pvalue(truediff, mean_diffs):
    """
    Calculate the p-value based on simulated means
    """
    return np.sum((truediff <= mean_diffs) + 1)/(len(meandiffs) + 1)

if __name__ == '__main__':
    print("P-Value: ", pvalue(true_m_diff, meandiffs))
