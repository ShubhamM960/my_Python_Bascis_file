#Powerful library for "data manipulation" and "data analysis" and can work with any type of tabular format type.

# why Pandas ?
# Ans : 
    #Efficient Data Handling
    #Data Alignment
    #Handling Missing Data 
    #Data Integration
    #Flexible Data Transformation
    
# Data Structure in Pandas : 
#     Series : 1-D Array i.e. - it represents the data of each column of the csv File(1-D)
#     Dataframes : 
#         - 2-D data structures with rows and columns .
#         - Combination of series
 
# https://pandas.pydata.org/docs/reference/series.html
# https://pandas.pydata.org/docs/reference/frame.html

##*Filtering DataFrame : 
    # ~ Sometimes we would need to remove the redundant or unnecessary data 
    # ~ filterout the rows and columns with missing values
    # ~ e.g. : filter with Column names, loc and iloc, based on condition
    
# DATA CLEANING :
    # ~ Finding null vales 
    # ~ Drop rows and columns with missing values (dropna(), )
    # ~ Fill the missing values with actual values (fillna())
    # ~ Handle duplicate values (drop_duplicate())

#Data Manipulation :
    # ~ drop(), replace(), apply()
    # ~sort_values('Columnname')
#Data Analysis :
    # ~groupby() and .agg()
    # ~ reset_index()