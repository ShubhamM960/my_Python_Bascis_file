##*
    #  series : it represents the data of each column of the csv File(1-D)
    #  Dataframe : it represents data of the multiple column of the csv file (2-D) 
# https://pandas.pydata.org/docs/reference/series.html
# https://pandas.pydata.org/docs/reference/frame.html

##*
# ========================================================================================================================
import pandas

#default seperate takes as ','  | if data.columns provide in a single string then use argument "sep"
data = pandas.read_csv("mycsv_python.csv", sep="\t") 
print(type(data)) #o/p : Dataframe
print(data)

# to get the columns name of the csv file
print(data.columns)         #o/p : Index(['Day', 'Temperature', 'Condition'], dtype='object')

print(type(data["Day"])) #o/p : Series

#O/P : print value for a particular column 
print(data['Day'])   # print(data.Day)

#============================================================

import pandas

data = pandas.read_csv("mycsv_python.csv", sep="\t")
data_dict = data.to_dict()

print(data_dict) # O/P : it represents the conentnt in the dictonary

print(data['Day'].to_list()) #O/p : print all the values of the column in a list
#========================================================