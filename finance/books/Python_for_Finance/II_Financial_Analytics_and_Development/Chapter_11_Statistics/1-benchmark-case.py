import numpy as np
#np.random.seed(1000)
import scipy.stats as scs
import statsmodels.api as sm
import matplotlib as mpl
import matplotlib.pyplot as plt

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
print(type(paths))

'''
plt.plot(paths[:, :10])
plt.grid(True)
plt.xlabel('time steps')
plt.ylabel('index level')
plt.show()
'''

log_returns = np.log(paths[1:], paths[0:-1])
