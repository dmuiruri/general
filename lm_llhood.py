#! /usr/bin/env python

"""
A module that demonstrates the use of log likelihood towards the
estimation of linear regression and robust regression. When estimating
the likelihood, we are estimating for the parameters of the model.

The maximum log-likelihood implementation below gets the maximum by
MINIMISING the NEGATIVE log-likelihood

A typical linear regression assumes that the estimation errors follow
a Normal distribution, however, a robust regression can be obtained by
using an alternative distribution of the error terms.

The Likelihood of a variable in a given distribution => pdf of that given variable
The log-likelihood of a variable in a given distn => log pdf version of the given dist


"""
import matplotlib.pyplot as plt
import autograd.numpy as np
import autograd
from scipy.optimize import minimize
from scipy.stats import norm

def linear_reg_normlogpdf(coefs, x, y):
    """
    Log likelihood for a linear regression where the error term
    follows a normal distribution see the normal dist pdf with mu=0
    std=1 in log
    
    The logpdf of normal distribution where x is the result of the
    func which being optimized in this case the error term (€). So we
    get the log-likelihood of the x in the normal distribution.

    Note: For some reason usint scipy.stats.norm.logpdf(x) does not
    work with autograd.
    """
    return np.sum(-0.5*np.log(2*np.pi)-0.5*(y - coefs[1] - coefs[0]*x)**2)


def linear_regression(x, y):
    """
    Estimate the linear regression coefficients using maximum
    likelihood estimation

    Setup the function to be optimized, which is the logpdf of the
    errors (€), the gradient of the function, which is setup by using
    autograd which performs gradient computations.
    """
    func = lambda c: -linear_reg_normlogpdf(c, np.array(x), np.array(y))
    d_func = autograd.grad(func) # gradient func
    v = minimize(func, np.ones(2), jac=d_func, method='L-BFGS-B')
    return v

def linear_reg_laplacelogpdf(coefs, x, y):
    """
    Create laplace model to estimate the distribution of the error
    term of a linear regression model
    """
    return np.sum(-np.log(2)-np.abs(y - coefs[1] - coefs[0]*x))

def laplace_regression(x, y):
    """
    Optimize the error function to obtain maximum likelihood of the
    parameters (const and Beta_1)
    """
    func = lambda c: -linear_reg_laplacelogpdf(c, np.array(x), np.array(y))
    d_func = autograd.grad(func)
    v = minimize(func, np.ones(2), jac=d_func, method='L-BFGS-B')
    return v

def w(x):
    """
    Generate weights to used in creating a normal mixture model. The
    generated weights follow the constraint that 0 ≤ π ≤ 1 and that
    the weights sum to 1 i.e π1 + ... + πk = 1. To achieve this
    contraints, transformations must be used.

    x is a scalar
    returns a vector of the weights [π1, π2] for a bivariate case
    """
    return np.array([1/(1 + np.exp(-x)), np.exp(-π)/(1 + np.exp(-x))])

def m_mv_logpdf(x, π, µ):
    """
    Generate a multivariate normal pdf.

    The logsumexp is used to generate the log of the sum of exponents
    generated from the function, "1" sums the values across the rows

    π is a function that performs a transformation and returns a 2d vector
    µ are 2D vector of means
    """
    return scs.logsumexp(np.log(π) + ss.norm.logpdf(x, µ, 1), 1)

def norm_mixture():
    """
    Generate parameter estimates using autograd and optimization
    (maximization)

    v is vector of optimized parameters with len similar to input vector

    The minimize function take the function and the input arguments in
    one vector, these elements can be distributed to the function by
    indexing the array as shown in the lambda function.

    In the lambda function, not the second argument is a function that
    returns a 2d vector, this allows the optimizer to reach and be
    able to optimize this function.
    """
    f = lambda a: -np.sum(m_mv_logpdf(d, w(a[0]), a[1:]))
    gf = autograd.grad(f) # gradient function
    v = minimize(f, [0.5, 1, 10.0], jac=gf, method='L-BFGS-B')
    return v

if __name__ == '__main__':
    # Compare a regular linear regression which assumes the errors
    # follow a Normal distrubution to a robust regression where the
    # errors are modelled as to follow laplace distribution.
#     x = np.arange(10)
#     y = np.copy(x); y[8]=0

#     v_norm = linear_regression(x, y)
#     print("Normal lr:", v_norm)
#     v_lap = laplace_regression(x, y)
#     print("Laplace lr:", v_lap)

    # Plot: Base on the plots, it is evident the laplace estimates the
    # model better while the normal distribution is more susceptible
    # to outliers or changes in the structure of the data.
#     t = np.array([0, 10])
#     plt.plot(x, y, '*')
#     plt.plot(t, v_norm.x[0]*t + v_norm.x[1], label='norm_lr')
#     plt.plot(t, v_lap.x[0]*t + v_lap.x[1], label='lap_lr')
#     plt.legend()
#     plt.show()


    # Maximum likelihood estimation of a normal mixture model
    v_norm_mix = norm_mixture()
    print(v_norm_mix)
    print("x, mu1, mu2:", p1(v_norm_mix.x[0]), v_norm_mix.x[1], v_norm_mix.x[2])
    t = np.linspace(0, 10, 100)
    ymv = m_mv_logpdf(t.reshape(len(t),1), w(v_norm_mix.x[0]), v_norm_mix.x[1:])
    plt.plot(x, np.exp(ymv))
    nb = plt.hist(d, 50, density=True)
