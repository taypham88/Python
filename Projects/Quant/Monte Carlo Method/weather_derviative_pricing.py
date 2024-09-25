'''Weather Derivatives'''

#Aim: We want to price temperature options'''
#Underlying HDD/CDD (heating/cooling degree days) index over given period

# Daily average temp is high + low //2
# HDD = (Tref - Tn)+
# CDD = (Tn - Tref)+
# AmountRecieve = function(DD) which is the sum of either the heating or cooling days.
# Cap on AmountRecieve (epsilon) = min(payrate(DD - K)+, C) C is the cap

import os
import numpy as np
import pandas as pd
import datetime as dt
from scipy import interpolate

import matplotlib.pyplot as plt

#Example
# temps = np.random.normal(65,5,92)
# HDD_p = np.maximum(0, 65 - temps)
# CDD_p = np.maximum(0, temps - 65)

# df = pd.DataFrame(np.array([temps,HDD_p,CDD_p]).T, index=range(1,len(temps)+1), columns = ['Aveg Temp', 'HDD', 'CDD'])
# df.loc['Total'] = pd.Series(df[['HDD', 'CDD']].sum())
# round(df,2)

