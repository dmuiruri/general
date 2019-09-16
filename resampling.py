#! /usr/bin/env python

"""
This module implements resampling strategies mainly PERMUTATIONS and
BOOTSTRAPPING
"""
import numpy as np
from pandas import DataFrame

np.random.seed(24)

data = DataFrame(np.random.randn(1500, 2))
x = data[0]
y = data[1]
sims = 1000

def mean_ci(no_of_sims=sims):
    """
    Compute the theoretical mean and the Bootstrap mean

    Use Bootsrtap to compute the mean confidence interval
    """
    means = np.zeros(no_of_sims)
    medians = np.zeros(no_of_sims)
    for i in range(no_of_sims):
        means[i] = np.mean(x.sample(x.shape[0], replace=True))
        medians[i] = np.median(x.sample(x.shape[0], replace=True))
    means_sig = np.std(means)
    medians_sig = np.std(medians)
    ci_mean_l = np.mean(means) - (1.96 * means_sig)
    ci_mean_u = np.mean(means) + (1.96 * means_sig)
    ci_med_l = np.mean(medians) - (1.96 * medians_sig)
    ci_med_u = np.mean(medians) + (1.96 * medians_sig)
    tci_mean_l = np.mean(x) - (1.96*np.std(x)/np.sqrt(len(x)))
    tci_mean_u = np.mean(x) + (1.96*np.std(x)/np.sqrt(len(x)))
    print("=====1).======")
    print("Theoretical mean: ", np.mean(x),",", "Estimated mean: ", np.mean(means))
    print("Theoretical confidence interval: ",tci_mean_l , "-", tci_mean_u)
    print("Estimated confidence interval: ", ci_mean_l, "-", ci_mean_u)
    print("=====2).======")
    print("Theoretical median: ", np.median(x),",", "Estimated median: ", np.mean(medians))
    print("confidence interval: ", ci_med_l, "-", ci_med_u)


