#! /usr/bin/env python

"""
Implementation of Density Estimation and Cross Validation

Density estimation: Given a sample drawn from a probability
distribution, how can we represent that distribution as a continuous
probability distribution.

Kernels: Gaussian Kernel, Uniform Kernel, Epanechnikov Kernel

Kernel Density Estimate: A formular that make use of a given kernel to
estimate the kernel density of a given point

Observations: The results are sensitive to the kernel bandwidth; When
"h" is too large in the case of a guassian kernel, the plot is very
thick, on the contrast, when "h" is too small, the density line
becomes too jagged.

Cross Validation can be used to tune the kernel bandwidth.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

d = pd.read_csv('http://www.cs.helsinki.fi/u/ahonkela/teaching/compstats1/toydata.txt').values

def K_gauss(x):
    """
    Generate the Gaussian Kernel for x

    This is for the univariate case, see multivariate version.
    """
    return (np.exp((-x**2)/2))/(np.sqrt(2*np.pi))

def K_ndgauss(x):
    """
    Get multivariate Gaussian Kernel
    
    x: An d dimensional array or dataframe with n observations
    """
    d = x.shape[1]
    return np.exp(-np.sum(x**2, 1)/2) / (np.sqrt(2*np.pi)**d)

def K_uniform(x):
    """ 
    Compute the uniform Kernel

    This is the univariate case
    """
    return 0.5 * (np.abs(x) < 1) 

def K_nduniform(x):
    """
    Generate the Multivariate Uniform Kernel

    x: An d dimensional array or dataframe with n observations
    """
    d = x.shape[1]
    return (0.5)**d * np.all((np.abs(x) < 1), 1)

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
    h: Kernel bandwidth
    """
    y = np.zeros(len(t))
    for i in range(len(t)):
        y[i] = np.mean(K_gauss((t[i] - x) / h)) / h
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

def cv_density_bandwidth(x):
    """
    Select "h", the kernel bandwidth.

    Using LOOCV (Leave One Out Cross Validation) technique to model
    the most suitable bandwidth parameter.

    Run the kernel_density multiple times (across all given "h") and
    taking log of the obtain density for every round of
    simulation.

    Step I (outer loop): Each round of simulation, one item is dropped
    from the passed array (x) which is the item left out (LOO). So for
    each stage, the simulation contains one element less of x.

    Step II (Inner loop): Note how logls are accumulated: All logls[0]
    contain the results of all cycles in step I where the simulation
    uses h[0] as the simulating kernel width.

    Once these are accumulated, the maximum of the stored values
    indicates which value of "h" among those given would maximize the
    objective function given. Therefore the optimal value of h is
    stored in a corresponding location as the maximum value
    location. (argmax) returns the indices of the maximum values along
    an axis.
    """
    h = np.linspace(0.1, 1.0, 10)
    logls = np.zeros(len(h))
    print("LOO-CV :")
    for i in range(len(x)):
        for j in range(len(h)):
            logls[j] += np.sum(np.log(kernel_density(x[i], np.delete(x, i), h[j])))
    return (h, h[np.argmax(logls)])

    
if __name__ == '__main__':
#     # Test 1
#     true_density_comparison()

#     # Test two
#     t = np.linspace(-2, 10, 100)
#     nb = plt.hist(d, 30, normed=True)

#     plt.plot(t, kernel_density(t, d, 3.0), label='h=3.0')
#     plt.plot(t, kernel_density(t, d, 1.0), label='h=1.0')
#     plt.plot(t, kernel_density(t, d, 0.3), label='h=0.3')
#     plt.plot(t, kernel_density(t, d, 0.1), label='h=0.1')
#     plt.legend()
#     plt.show()
    
    # Test 3
    print(cv_density_bandwidth(d))
