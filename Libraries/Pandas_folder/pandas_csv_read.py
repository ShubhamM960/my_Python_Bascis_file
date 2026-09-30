### ====== SERIES ================
import pandas as pd
d = {"a": 1, "b": 2, "c": 3}
ser = pd.Series(d)
print(ser)

cities = ['Kolkata', 'Chicago', 'Toronto', 'Lisbon']
populations = [14.85, 2.71, 2.93, 0.51]
city_series = pd.Series(populations, index=cities)
print(city_series)

### ================ DATA FRAMES ================
import pandas as pd
import numpy as np
d = {"col1": [1, 2], "col2": [3, 4]}
df = pd.DataFrame(data=d)
print(df)


df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Aritra'],
                   'Age': [25, 30, 35],
                   'Location': ['Seattle', 'New York', 'Kona']},
                  index=([10, 20, 30])
                )
print(df)
# O/P : 
#      Name  Age  Location
# 10   Alice   25   Seattle
# 20     Bob   30  New York
# 30  Aritra   35      Kona

df = pd.DataFrame(
    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["a", "b", "c"]
    )
print(df)
# O/P : 
#    a  b  c 
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9

cities = pd.Series(['Kolkata', 'Chicago', 'Toronto', 'Lisbon'], name = 'City')
populations = pd.Series([14.85, 2.71, 2.93, 0.51], name = 'Population')
df = pd.concat([cities, populations], axis = 1)
print(df)
# O/P :
#     City  Population
# 0  Kolkata       14.85
# 1  Chicago        2.71
# 2  Toronto        2.93
# 3   Lisbon        0.51
# ========================================================================================================================
import pandas

#default seperate takes as ','  | if data.columns provide in a single string then use argument "sep"
data = pandas.read_csv("mycsv_python.csv", sep="\t") 
print(type(data)) #o/p : Dataframe
print(data)       #O/P : Print all the rows and columns of the CSV file

# to get the columns name of the csv file
print(data.columns)         #o/p : Index(['Day', 'Temperature', 'Condition'], dtype='object')

print(type(data["Day"])) #o/p : Series

#O/P : print all values for a particular column 
print(data['Day'])   # print(data.Day)

#============================================================

import pandas

data = pandas.read_csv("mycsv_python.csv", sep="\t")
data_dict = data.to_dict()

print(data_dict) # O/P : it represents the conentnt in the dictonary

print(data['Day'].to_list()) #O/p : print all the values of the column in a list
#========================================================