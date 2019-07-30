import pandas as pd 
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt 
import statsmodels.api as sm
import statsmodels.formula.api as smf
import math





#========= Making a dataframe and creating a series ===============



Southphoenix =  pd.read_csv('southphoenix.csv', header = 0, squeeze = True, 
    usecols = [3,6], na_values = -999)
print(Southphoenix)

#Southphoenix['dates'] = Southphoenix['utc'].astype('datetime64')

#Southphoenix.loc['2018-10-01T00:00:00.000Z':'2018-08-18T01:00:00.000Z']


table1 = pd.Series(Southphoenix['value'].values.copy(),
    Southphoenix['utc'].values.copy())




#========== Scatter plot ==============

Southphoenix['value'].plot(linestyle = '', marker = 'o', markersize = 2)

Southphoenix.sort_index(axis = 0)

axis = plt.gca()




axis.set_title("South Phoenix Pollution", fontsize = 25, color = "Black", )


axis.set_ylabel(r'Air Quality PM2.5', fontsize = 25, color = "Black")

axis.set_xlabel(r'Time Period', fontsize = 25, labelpad = 50, color = "Black")

axis.set_xticklabels(Southphoenix['utc'], fontsize = 8)
plt.xticks(rotation = '5')

plt.subplots_adjust(top=0.9, bottom = 0.32)

#axis.set_yticklabels(Southphoenix['value'], fontsize = 5)

axis.set_facecolor("cornsilk")

#=================================




#========== plotting regression line ===========

SD = pd.Series(data=Southphoenix['value'].values).dropna()

ax = plt.gca()

xticks = ax.get_xticks()

x = np.linspace(xticks[0], xticks[-1], len(SD))
X = sm.add_constant(x)
model = sm.OLS(SD, X)
result  = model.fit()
y_line = result.params['x1'] * xticks + result.params['const']


plt.plot(xticks, y_line, linewidth= 2, color = 'Black')




r = pd.Series(xticks).corr(SD)
ax.text(xticks[1], 600, "Pearson's r =" + str(round(r, 2)), fontsize=30)




ax.set_xlim(0, 1400)



plt.show()


print(result.params)
print(result.summary)







