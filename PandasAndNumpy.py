
#importing libraries
import numpy as np
import pandas as pd

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

np.mean(my_series)

"""Data Frame Creation and Indexing

"""

#Create dictionary with different data type as value

my_dict={"Name":["Ram","Shyam","Hari"],
         "Age":np.array([10,15,20]),
         "Weight":(60,65,70),
         "Height":pd.Series([5.5,5.8,6],index=["Ram","Shyam","Hari"]),
          "Siblings":1,
         "Gender":"M"
}
df=pd.DataFrame(my_dict)  #Converts dict to DataFrame
df



df2=pd.DataFrame(my_dict,index=my_dict["Name"])
df2

df2["Weight"]

df2.Height

# needs to pass 3 value with size of the dataset
df2["IQ"]=[100,90,105]
df2

#Gives specific data of given Key value
df.loc["Ram"]

df.loc["Ram":"Hari","Age":"Height"] #slicing through label

df2["Married"]=False

df2

boolean_index=[False,True,True]
df2[boolean_index]

boolean_index=df2["Age"]>12