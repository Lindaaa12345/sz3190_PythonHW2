import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    periods = m * ppy
    cash_flows = np.full(periods, face * couponRate / ppy)
    time_periods = np.arange(1, periods + 1)
    discount_factors = (1 + y / ppy) ** -time_periods
    pv_coupons = cash_flows * discount_factors
    pv_face = face / ((1 + y / ppy) ** periods)
    
    return np.sum(pv_coupons) + pv_face

# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
