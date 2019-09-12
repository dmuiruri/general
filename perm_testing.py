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

# print(data.describe())

Nperms = 1000 # No of permutations

# Generate male female masks
# Imale = (fram['SEX'] == 'male').values
# Ifemale = (fram['SEX'] == 'female').values

m_mean_age = np.mean(data['AGE'][data['SEX'] == 'male'])
f_mean_age = np.mean(data['AGE'][data['SEX'] == 'female'])

print("True mean difference {}".format(m_mean_age - f_mean_age))

# if __name__ == '__main__':
