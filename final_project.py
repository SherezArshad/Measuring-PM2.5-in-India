import pandas as pd 
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt 
import statsmodels.api as sm
import statsmodels.formula.api as smf
import math
import random


#step 1: read dataframe into a variable pd.read_csv()
#step 2: clean up data, get rid of any negative 999 values and set negative values in data to 0. (pandas)

#step 3: create x(local time) and y(values) variable values. (time) create time series (datetime objects)
#step 4: Make a new dataframe and plot any graph of liking.
#step 5: Tidy up graph add color (legend)
#step 6: Plot regression line. 

 # df.dtypes = to check what types are in the df. 

# Do three different graphs based on 3 different months. Plot graph for August First


#Step 1: Read file into a dataframe
Phoenix = pd.read_csv('westphoenix.csv', header = 0, squeeze = True,
    usecols = [4,6], na_values = -999)
print(Phoenix)

Phoenix['dates'] = Phoenix['local'].astype('datetime64')


airquality = pd.Series(Phoenix['value'].values.copy(), 
    Phoenix['local'].values.copy())


september = airquality.loc['2018-09-06T07:00:00-07:00':'2018-09-06T23:00:00-07:00']





sith = Phoenix['value'].plot.line()



# Stp 3: Style the graph, add titles, fontsizes, etc

axis = plt.gca()


axis.set_title("West Phoenix Pollution", fontsize = 30, color = "Black")


axis.set_ylabel(r'Air Quality PM25', fontsize = 20, color = "Black")

axis.set_xlabel(r'Local Time', fontsize = 20, color = "Black")

axis.set_facecolor("azure")

axis.set_xticklabels(Phoenix['local'], fontsize = 8)

plt.xticks(rotation = '6')



#plt.gcf().set_facecolor("#E3CF57")


#plt.plot()
plt.show()



#===========================


# parse datestrings, 

#columns location, city, country, utc, local, parameter, value, unit, latitude, longitude, attritbution

#Figure out the defination of values (know what your variables are)

