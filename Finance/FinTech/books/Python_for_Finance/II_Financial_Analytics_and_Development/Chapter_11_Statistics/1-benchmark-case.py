import numpy as np
#np.random.seed(1000)
import scipy.stats as scs
import statsmodels.api as sm
import matplotlib as mpl
import matplotlib.pyplot as plt


def print_statistics(array):
    ''' Prints selected statistics.

    Parameters
    ==========
    array: ndarray
        object to generate statistics on
    '''
    sta = scs.describe(array)
    print("%14s %15s" % ('statistic', 'value'))
    print(30 * "-")
    print("%14s %15.5f" % ('size', sta[0]))
    print("%14s %15.5f" % ('min', sta[1][0]))
    print("%14s %15.5f" % ('max', sta[1][1]))
    print("%14s %15.5f" % ('mean', sta[2]))
    print("%14s %15.5f" % ('std', np.sqrt(sta[3])))
    print("%14s %15.5f" % ('skew', sta[4]))
    print("%14s %15.5f" % ('kurtosis', sta[5]))


def gen_paths(s0, r, sigma, T, M, I):
    ''' Generates Monte Carlo paths for geometric Brownian motion.

    Parameters
    ==========
    s0 : float
        initial stock/index value
    r : float
        constant short rate
    sigma : float
        constant volatility
    T : float
        final time horizon
    M : int
        number of time steps/intervals
    I : int
        number of paths to be simulated

    Returns
    =======
    paths : ndarry, shape (M + 1, I)
        simulated paths given the parameters
    '''
    # Create M+1*I array and initilize them to 0
    dt = float(T) / M
    paths = np.zeros((M + 1, I), np.float64)
    # Initilize the first row to s0.
    paths[0] = s0
    for t in range(1, M + 1):
        # Create I numbers are standard normal distributed
        rand = np.random.standard_normal(I)
        # Use Z-Score normalization. converted to standard normal distribution?
        rand = (rand - rand.mean()) / rand.std()
        # Use Black-Scholes-Merton to simulate the future price.
        paths[t] = paths[t - 1] * np.exp((r - 0.5*sigma**2) * dt + sigma * np.sqrt(dt) * rand)
    return paths

s0 = 100.
r = 0.05
sigma = 0.2
T = 1.0
M = 50
I = 15
paths = gen_paths(s0, r, sigma, T, M, I)
print(paths.round(4))

'''
plt.plot(paths[:, :10])
plt.grid(True)
plt.xlabel('time steps')
plt.ylabel('index level')
plt.show()
'''

log_returns = np.log(paths[1:] / paths[0:-1])
print(log_returns.round(4))

print_statistics(log_returns.flatten())
