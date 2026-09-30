##################  DATA MANIPULATION ###################
######################################################

###############     Read CSV    ##################
import pandas as pd

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/organizations-duplicates-1000.csv"
data = pd.read_csv(file_path)
#print (data)
#print(data.info())
print(data.head()) #print(data.head(20))
#print(data.columns)
print(data.describe())


###############################################################
####### F I L T E R with PANDAS dataframe / Series ############
################################################################
#using "Columns"
import pandas as pd

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/organizations-duplicates-1000.csv"
data = pd.read_csv(file_path)

print(data[ 'Name' ]) # for one column
print(data[ ['Name','Website', 'Industry'] ] ) # to provide multiple columns values
#===========================
# .loc(row_index, Columnname)      : find the particular value of 'n'th row of "columnname"
#  .iloc(row_index, column_index)   : find the particular value of 'n'th row of 'm'th column
import pandas as pd 
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Aritra'],
                   'Age': [25, 30, 35],
                   'Location': ['Seattle', 'New York', 'Kona']},
                  
                )
print(df.loc[1, 'Age']) # 30
print(df.iloc[0,2]) # Seattle

#iloc with SLICING
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Aritra'],
                   'Age': [25, 30, 35],
                   'Location': ['Seattle', 'New York', 'Kona']},
                  
                )
print(df.loc[0:2, 'Age']) 
print(df.iloc[0:2,0:2]) #print(df.iloc[0:2,0])

#==============================
#using "CONDITIONS"
import pandas as pd

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/organizations-duplicates-1000.csv"
data = pd.read_csv(file_path)

print( data[ data['Number of employees'] > 2000 ] ) # show the filter data with all columns
print( data[ data['Number of employees'] > 2000 ]['Number of employees'] ) # show the filter data with one specific column
print( data[ data['Number of employees'] > 2000 ] [ ['Organization Id', 'Number of employees'] ] ) # show the filter data with selected columns 

#multiple conditions

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/organizations-duplicates-1000.csv"
data = pd.read_csv(file_path)
print( data[ (data['Number of employees'] > 2000) & (data['Country'] == 'Uzbekistan') ]) 
#========================================================================================


#mean(), max(), min()
import pandas as pd

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/organizations-duplicates-1000.csv"
data = pd.read_csv(file_path)
print(data['Number of employees'].mean()) # Avg of number of employess considering aLL THE ROWS

#find the means of orgaization employee count > 2000
print( data[ data['Number of employees'] > 2000 ] [ 'Number of employees'].mean() )

print(data['Number of employees'].max()) 
print(data['Number of employees'].min())

#==========================================================================================

#Frequently use / common value value in a column  ".mode()""
import pandas as pd

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/organizations-duplicates-1000.csv"
data = pd.read_csv(file_path)
print(data['Country'].mode()) #O/P : return the frequently use values of the column in a LIST
print(data['Country'].mode()[0])#O/P : return the first value of frequently use values of the column



###############################################################
##### H A N D L I N G   M I S S I N G values with  PANDAS #####
################################################################
 #Drop Null values : dropna(), isna()
import pandas as pd

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/people-100.csv"
data = pd.read_csv(file_path)
print(data.dropna())
data.dropna(inplace = True) #change the original Dataframe
print(data.isna().sum()) #provide sum of rows having null / blank/ NAN for each column
#print(data['Country'].isna().sum()) #provide sum of rows having null / blank/ NAN for specific column


#=======================================================================
#FILL the NAN / NULL / BLANK values : fillna(), 

import pandas as pd

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/people-100.csv"
data = pd.read_csv(file_path)

# Fill the blank value in a column with specific value
data['Age'] = data['Age'].fillna( 30 )  #data['Age'].fillna( 30, inplace = True )

# Fill the blank value in a column with mean value 
data['Age'] = data['Age'].fillna( data['Age'].mean() )
## Fill the blank value in a column with frequently use  value 
data['Country'] = data['Country'].fillna( data['Country'].mode()[0] )

# print(data['Age'].isna.sum()) #O/P : 0
# print(data['Country'].isna.sum())

##=======================================================================



#apply(), replace(), drop()

#.apply() ; Use to perform some custom operation 
    #apply(FunctionName) or apply(lambda var : Expression)
    
import pandas as pd

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/organizations-duplicates-1000.csv"
data = pd.read_csv(file_path)

data['Eligible Org'] = data['Number of employees'].apply(lambda x : x > 2000)

print(data['Eligible Org'])

#===================
#drop(columnname , axis = 1) : to drop a particular column 
#drop(rownumber , axis = 0) : to drop a particular row 
import pandas as pd

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/people-100.csv"
data = pd.read_csv(file_path)

print(data.drop(3, axis = 0 )) # drop the 3rd row from the 
print(data.drop('First Name', axis = 1 )) #drop the entire ''First Name'' column
#=======================================================================

#sort the data based on a specific column ,       sort_values('ColumnName')
import pandas as pd

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/people-100.csv"
data = pd.read_csv(file_path)

print( data.sort_values('Date of birth') ) #ascending order  and all the columns
print( data.sort_values('Date of birth', ascending= False)  ) #descending order and all the columns
print( data.sort_values('Date of birth') ['First Name'] ) #ascending order  and one specific column
print( data.sort_values('Date of birth') [ ['First Name', 'Phone','Job Title', ]] ) #ascending order  and with specific columns

    #multile columns sorting
print( data.sort_values(['Date of birth', 'First Name']) )
print( data.sort_values(['Date of birth', 'First Name'], ascending=[True, False]) )

##============================================================================

#drop_duplicates(): Removes duplicate rows from the DataFrame.
import pandas as pd

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/people-100.csv"
data = pd.read_csv(file_path)
print(data.drop_duplicates())
data.drop_duplicates(inplace = True)