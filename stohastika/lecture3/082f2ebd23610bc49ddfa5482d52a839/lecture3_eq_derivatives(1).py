import numpy as np
import scipy.stats as ss

# Black and Scholes
def d1(S0, K, r, sigma, T):
    return (np.log(S0 / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))


def d2(S0, K, r, sigma, T):
    return (np.log(S0 / K) + (r - sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))


def BlackScholes(type, S0, K, r, sigma, T):
    if type == "C":
        return S0 * ss.norm.cdf(d1(S0, K, r, sigma, T)) - K * np.exp(-r * T) * ss.norm.cdf(d2(S0, K, r, sigma, T))
    else:
        return K * np.exp(-r * T) * ss.norm.cdf(-d2(S0, K, r, sigma, T)) - S0 * ss.norm.cdf(-d1(S0, K, r, sigma, T))

def C(S0, t, K, T, r = 0, sigma = 0.2):
    return BlackScholes("C", S0, K, r, sigma, T - t)

S0 = 1.0
K = 1.0
T = 1.0
sigma = 0.2
r = 0

# lets plot it!
import matplotlib.pyplot as plt

spots = np.linspace(0.5, 1.5, 50)
calls = [C(s, 0, K, T) for s in spots]
payoff = [np.max([s-K, 0]) for s in spots]
plt.figure("Call price  as a function of spot")
plt.plot(spots, calls)
plt.plot(spots, payoff)
plt.show()

#do your sanity checks here


def dailyPnL(prev_S, curr_S, prev_t, curr_t):
    prev_C = C(prev_S, prev_t, K, T)
    curr_C = C(curr_S, curr_t, K, T)

    #pnl from short option position
    optionPnL = - (curr_C- prev_C)

    #pnl from cash account with option premium
    optionPremiumInterestPnL = r * prev_C * (curr_t - prev_t)

    #pnl from delta hedge
    prev_delta = ( C(prev_S + 0.01, prev_t, K, T) - C(prev_S, prev_t, K, T) ) / 0.01

    deltaHedgePnL = prev_delta * (curr_S - prev_S)

    #interest you pay on the cash you borrow to buy delta hedge
    deltaHedgeInterestPnL = r * prev_delta * prev_S * (curr_t - prev_t)

    return deltaHedgePnL + optionPnL + deltaHedgeInterestPnL + optionPremiumInterestPnL


def TotalPnL(path, timeline):
    nbSteps = len(path)

    totalPnL = 0

    for i in range(1, nbSteps):
        prev_S = path[i-1]
        prev_t = timeline[i-1]
        curr_S = path[i]
        curr_t = timeline[i]
        totalPnL = totalPnL + dailyPnL(prev_S, curr_S, prev_t, curr_t)

    return totalPnL

# numerics
nbStepsPerYear = 252

# Monte-Carlo engine code start
def getPathAndTimeline(spot, T, mu=0, sigma=0.2, noiseGen = lambda x : np.random.randn()):
    # returns a simulated path of the stock

    # propagator
    def dS(S, mu, sigma, dt, noise):
        return S * mu * dt + S * sigma * np.sqrt(dt) * noise

    #some numerical setup
    nbStepsPerYear = 250
    nbSteps = (int) (nbStepsPerYear * T)
    path = np.zeros(nbSteps)
    timeline = np.zeros(nbSteps)
    dt = T / nbSteps

    #our path starts from the current spot
    path[0] = spot

    #propagate the path according to the model
    for i in range(1, nbSteps):
        S = path[i-1]
        noise = noiseGen(i)
        S_next = S + dS(S, mu, sigma, dt, noise)
        path[i] = S_next
        timeline[i] = timeline[i-1] + dt

    return path, timeline

#Let's play!
#Check that the total PnL on average is zero

nbIter = 100
pnl=np.zeros(nbIter)
for i in range(nbIter):
    path, timeline = getPathAndTimeline(S0, T)
    pnl[i] = TotalPnL(path, timeline)

print("On average total Pnl after hedging is %.3f"%np.average(pnl))