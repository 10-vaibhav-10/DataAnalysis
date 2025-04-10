#importing libraries
import numpy as np # type: ignore
import pandas as pd # type: ignore

my_series=pd.Series( index=['a','b','c','d'],
                    data=[1,2,3,4] )#Data #indexes
my_series
#We assigned label their index value along with the data

my_dict={"a":1,"b":2,"c":3,"d":4}
my_series=pd.Series(my_dict)
my_series

# we can just access item from series by using label
my_series['c']

my_series[0]
#it goes through index number

#the slicing on series gives label and data
my_series[0:2]

my_series+my_series