import csv

#open file
with open('mycsv_python.csv', encoding= 'utf-8', sep = '\t') as csv_file: 
    #csv reader
    csv_data = csv.reader(csv_file)

    #reformat into python object list of list ==> Each row of the csv file represent a list stores into aa another list i.e. :- [ [a,b,c], [e,f,g] ]
    data_lst = list(csv_data)

    print(data_lst)
    print(data_lst[0])
    csv_file.close()

#===============================================

import csv

#open file
with open('mycsv_new.csv', mode = 'a', newline='', encoding = 'utf-8') as csv_file :

    data_write = csv.writer(csv_file, delimiter= ',')

    data_write.writerow(['a','b','c','abc@gmail.com', 18])
    data_write.writerows(['x','y','z','aderx@gmail.com', 18], ['s','t','u','werwtw@gmail.com', 78])
    
    csv_file.close()

#===============================================

import csv

#open file
csv_file = open('mycsv_new.csv', mode = 'w', newline='', encoding = 'utf-8')

data_write = csv.writer(csv_file, delimiter= ',')
data_write.writerow(['a','b','c','abc@gmail.com', 18])
data_write.writerows(['x','y','z','aderx@gmail.com', 18], ['s','t','u','werwtw@gmail.com', 78])

csv_file.close()
