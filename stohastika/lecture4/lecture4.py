import numpy as np
import matplotlib.pyplot as plt

# short rate model

rawYieldCurve = {
                "ON": {"T": 1./365, "yield": 0.0755},
                "1W": {"T": 7./365, "yield": 0.0758},
                "2W": {"T": 14./365, "yield": 0.0758},
                "1M": {"T": 30./365, "yield": 0.0752},
                "2M": {"T": 60./365, "yield": 0.0743},
                "3M": {"T": 90./365, "yield": 0.0739},
                "6M": {"T": 1./2., "yield": 0.0738},
             }

class YieldCurve:
    def __init__(s, rawYields):
        s.rawYields = rawYields

    def yieldToRate(s, y, t):
        return np.log(1.0 + y * t) / t

    def rateToYield(s, rate, t):
        return (np.exp(rate * t) - 1.0) / t

    def getYield(s, expiry):
        timeline = [s.rawYields[key]['T'] for key in s.rawYields]
        rates = [s.yieldToRate(s.rawYields[key]['yield'], s.rawYields[key]['T']) for key in s.rawYields]
        rate = np.interp(expiry, timeline, rates)
        return s.rateToYield(rate, expiry)


def yieldToRate(y, t):
    return np.log(1.0 + y*t)/t

def rateToYield(rate, t):
    return (np.exp(rate*t)-1.0)/t

def getYield(expiry, curve):
    timeline = [curve[key]['T'] for key in curve]
    rates = [yieldToRate(curve[key]['yield'], curve[key]['T']) for key in curve]
    rate = np.interp(expiry, timeline, rates)
    return rateToYield(rate,expiry)

#Fantastic! I know yield for any time point! I can price a simple swap
# Let's put together a few classes to do that

class Swap:
    def __init__(s, receiveLeg, payLeg):
        s.receiveLeg = receiveLeg
        s.payLeg = payLeg

    def getNpv(s, curve):
        return - s.payLeg.getNpv(curve) + s.receiveLeg.getNpv(curve)

    def __str__(s):
        description = "---SWAP---\n"+"payLeg: " + s.payLeg.__str__() + "\n" + "receiveLeg: " + s.receiveLeg.__str__() + "\n----------"
        return description

class Leg:
    def __init__(s, cashflows):
        s.cashflows = cashflows

    def __str__(s):
        description=""
        for cashflow in s.cashflows:
            description += cashflow.__str__()
        return description

    def getNpv(s, curve):
        npv = 0
        for cashflow in s.cashflows:
            npv += cashflow.getNpv(curve)
        return npv

class Cashflow:
    def __init__(s, amount, payTime):
        s.amount = amount
        s.payTime = payTime

    def getNpv(s, curve):
        #return s.amount / (1.0 + getYield(s.payTime, curve)*s.payTime)
        return s.amount / (1.0 + curve.getYield(s.payTime) * s.payTime)

    def __str__(s):
        return "(%.3f RUB at %.3f)\n"%(s.amount, s.payTime)


class FloatCashflow(Cashflow):
    def __init__(s, nominal, start, end, yc):
        s.nominal = nominal
        s.start = start
        s.end = end
        Cashflow.__init__(s, s.getAmount(yc), s.end)

    def getAmount(s, curve):
        duration = (s.end - s.start)
        futureRate = ((1.0 + curve.getYield(s.end) * s.end)/(1.0 + curve.getYield(s.start) * s.start) - 1.0) / duration
        amount = s.nominal * (1.0 + futureRate * duration)
        return amount



# Let's try!
yc = YieldCurve(rawYieldCurve)

fcf = FloatCashflow(1e6, 2.0/12, 3./12, yc)

print(fcf)
print("FloatingCashFlow Npv = %.3f" %fcf.getNpv(yc))

payLeg = Leg([Cashflow(1e6, 1./12),
              Cashflow(1e6, 2./12),
              FloatCashflow(1e6, 2.0/12, 3./12, yc),
              Cashflow(1e6, 4./12),
              Cashflow(1e6, 5./12),
              Cashflow(1e6, 6./12)])

receiveLeg = Leg([Cashflow(6e6, 6./12)])


ourSwap = Swap(receiveLeg, payLeg)
npv = ourSwap.getNpv(yc)

print(ourSwap)
print("Swap price is %.3f"%npv)

