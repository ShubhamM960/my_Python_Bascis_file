##################  DATA ANALYSIS ###################
######################################################
### groupby '<columnname>'
     #groupby use with any column    
import pandas as pd

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/organizations-duplicates-1000.csv"
data = pd.read_csv(file_path)

print(data.groupby('Country'))
print(data.groupby('Number of employees').mean())
print( data.groupby(['Country', 'Organization Id' ]) )      


# .agg({ 'columnname1' : 'mathematical function' , 'columnname2' : mathematical function'})
    # 'agg' use "mathematical functions" means only applicable with numeriacal columns(int, float)
 
import pandas as pd

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/organizations-duplicates-1000.csv"
data = pd.read_csv(file_path)

print(data.groupby('Country').agg(
    {
        'Number of employees' : 'mean'
    }
)) #data.groupby('Country')['Number of employees'].mean()

#data.groupby('Country', 'Organization Id' ])['Number of employees'].mean()



#group records by "product category" and calculate the average price and total quantity:
import pandas as pd
data = {
    "Product": ["Laptop", "Phone", "Shirt", "Jeans", "Tablet"],
    "Category": ["Electronics", "Electronics", "Clothing", "Clothing", "Electronics"],
    "Price": [1000, 600, 30, 50, 400],
    "Quantity": [2, 5, 10, 6, 3]
}
df = pd.DataFrame(data)
result = (
    df.groupby("Category").agg(
        {
             "Price" : "mean",
            "Quantity" : "sum"
        }
         
      )
)
print(result)
#=============================================================================================
#reset_index() : It creates a index column
import pandas as pd

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/organizations-duplicates-1000.csv"
data = pd.read_csv(file_path)

group_data = data.groupby('Country').agg(
    {
        'Number of employees' : 'mean'
    }
).reset_index()

print(group_data)
#=============================================================================================


import pandas as pd

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/organizations-duplicates-1000.csv"
data = pd.read_csv(file_path)

group_data = data.groupby('Country').agg(
                {
                    'Number of employees' : 'mean'
                }
            )

print(f"loc use : {group_data.loc[ 10, 'First Name' ]}" )
print(f"loc use : {group_data.iloc[ 3, 4 ]}" )

#=======================================================================
#concat( [ dataframe1, dataframe2 ] , axis = ) : 
    # ~ axis = 0 --> concate horizontally (row wise)
    # ~ axis = 1 --> concate vertically   (column wise)
    

    
#merge(df1, df2, on=, how=) :
    # merging the dataframes based on a common "COLUMN" or "INDEX"
    # on = 'COMMON_COLUMN_NAME'
    # how = inner ,outer, left, right
import pandas as pd

employees = pd.DataFrame({
    "employee_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
})
salaries = pd.DataFrame({
    "employee_id": [1, 2, 4],
    "salary": [70000, 80000, 90000]
})

def merge_dataframes(
    left_df: pd.DataFrame,
    right_df: pd.DataFrame,
    index: str | list[str],
    how: str = "inner" ) -> pd.DataFrame:
    """Merge two DataFrames using one or more common columns."""
    return pd.merge(left_df, right_df, on = index, how=how)
result = merge_dataframes(
    employees,
    salaries,
    index="employee_id",
    how="left"
)
print(result)
#==========================================

import pandas as pd
import emotions
emotions.set_format(tpe = 'pandas')
df = emotions['train'][:]
df.head()