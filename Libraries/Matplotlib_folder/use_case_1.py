import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#Line Chart :
    #.plot(x,y)
months = ['Jan', 'Feb', 'March', 'April', 'May']
sales = [23000, 31512, 17903, 45094, 21436]
plt.xlabel('months')
plt.ylabel('sales')
plt.plot(months, sales, marker = 'o', color = 'b', linestyle = '--')
print(plt.show())

#Scatter chart
    #.scatter(x,y)
    
df = pd.DataFrame({
        'OrderId' : [1,2,3,4,5,6,7,8,9,10],
        'OrderQuantity' : [13,23,34,21,23,36,11,9,28,12],
        'TotalAmount' : [65,115,135,105,104,150,55,50,140,67]
    })
plt.xlabel('OrderId')
plt.ylabel('TotalAmount')
plt.scatter(df['OrderId'], df['TotalAmount'], color = 'g', edgecolors='black')
#plt.grid(True)
print(plt.show())

#bubble chart 
    #.scatter(x,y)
   
catagories = ['grocery', 'health and beauty', 'office supplies', 'entertainments']
share = [0.1,0.2,0.3, 0.4, 0.5]
avg_growth = [0.22, 0.33, 0.25, 0.4, 0.5]
total_sales = [200, 500, 800, 200, 500]

plt.scatter(share, avg_growth, color = ['blue', 'green', 'red', 'cyan', 'yellow'], s = total_sales)

for i, catagory in enumerate(catagories) :
    plt.text(share[i], avg_growth[i], catagory, ha = 'center')
    
plt.xlabel('Share of total revenue')
plt.ylabel('Growth')
plt.title('E-Commerce by catagory')
plt.show()


#histogram : 
   #plt.hist(x, bins = <number>, edgecolor = , color = )
    #x = list of data we want to display (generally it is list of number )
    # bins =  how many groups (or which ranges) the values are put into each bin or one bar. i.e : number of bars we want to show to display for whole data 
ages = [12, 15, 18, 22, 22, 25, 30, 35, 40, 41, 42, 50]
plt.hist(ages, bins=5, edgecolor = 'black', color='green')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

#barchart :
    #.bar()
catagories = ['Electronics', 'Clothing', 'Accessories', 'Beauty', 'Home Appliences']
revenues  = [20000, 3600, 41003, 10000, 15000]
plt.bar(catagories, revenues, color=['b', 'g', 'r', 'y', 'c']) #x-axis = category name, y-axis = value to display
plt.xlabel('Catagories of Product')
plt.ylabel('revenue')
plt.show()

#piechart: 
    #.pie(x, label = <list of names to display>)
catagories = ['Electronics', 'Clothing', 'Accessories', 'Beauty', 'Home Appliences', 'Others']
percentage  = [16, 22, 21, 12, 18, 11]
plt.pie(percentage, labels= catagories, autopct='%.1f%%' ) #x-axis = category name, y-axis = value to display
plt.title('Catagories of products ')
plt.show()


companies = ['Meta', 'Amazon', 'Apple', 'Netflix', 'Google', 'SapceX', 'Tesla', 'Youtube', 'MI', 'OpenAI', 'Uber']
share = [0.12, 0.16, 0.22, 0.04, 0.18, 0.05, 0.08, 0.06, 0.02, 0.04, 0.03]
plt.pie(share, labels=companies, autopct='%.1f%%')
plt.title('Share by Companies')
plt.show()

#Heatmap : 
    #.iamshow(x, cmap = , interpolation = )
    #
    
    
#subplot(row, column, index) :
companies = ['Meta', 'Amazon', 'Apple', 'Netflix', 'Google', 'SapceX', 'Tesla', 'Youtube', 'MI', 'OpenAI', 'Uber']
share = [0.12, 0.16, 0.22, 0.04, 0.18, 0.05, 0.08, 0.06, 0.02, 0.04, 0.03]
plt.title('Share by Companies')
plt.subplot(1,2,1)
plt.pie(share, labels=companies, autopct='%.1f%%')


months = ['Jan', 'Feb', 'March', 'April', 'May']
sales = [23000, 31512, 17903, 45094, 21436]
plt.xlabel('months')
plt.ylabel('sales')
plt.subplot(1,2,2)
plt.plot(months, sales, marker = 'o', color = 'b', linestyle = '--')

plt.show()