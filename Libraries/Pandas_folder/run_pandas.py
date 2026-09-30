import pandas as pd

file_path = "/Users/smehe475/Python Practice/Pandas_folder/CSV Data files/organizations-duplicates-1000.csv"
data = pd.read_csv(file_path)
print( data[ (data['Number of employees'] > 2000) & (data['Country'] == 'Uzbekistan') ]) 