
import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    periods = m * ppy
    time_periods = np.arange(1, periods + 1)
    cash_flows = np.full(periods, (face * couponRate) / ppy)
    cash_flows[-1] += face  
    discount_factors = (1 + y / ppy) ** -time_periods
    pv_cash_flows = cash_flows * discount_factors
    weights = pv_cash_flows / pv_cash_flows.sum()
    duration = np.sum(weights * time_periods)
    
    return duration


# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1

