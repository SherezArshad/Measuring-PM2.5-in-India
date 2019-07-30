import pandas as pd 
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt 
import statsmodels.api as sm
import statsmodels.formula.api as smf
import math


#=====================


tempe =  pd.read_csv('Tempe.csv', header = 0, squeeze = True,
    usecols = [6], na_values = -999)

print(tempe)




#aug_sep_oct = tempe.loc['2018-08-18T01:00:00.000Z':'2018-10-23T00:00:00-07:00']


#tempe['dates'] = tempe['utc'].astype('datetime64')


#======================



#tempe = pd.Series(tempe['value'].values.copy(), tempe['utc'].values.copy())

#size, scale = 100, 10

#tempe = pd.Series(np.random.gamma(scale, size= size) ** 1.5)

tempe.plot.hist(grid=True, bins=15, rwidth=0.9,
                   color='#607c8e')

#axis = plt.gca()




plt.title('Tempe, Phoenix Pollution')
plt.xlabel('PM2.5 Concentration range')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)




ax = plt.gca()
ax.set_xlim(-5, 25)
plt.show()


































