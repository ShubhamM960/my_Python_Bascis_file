import numpy as np

# arr = [1,4.5, 'Ssm', {'key1' : 'val1'}, [1,2,3]]
# print(np.array(arr)) # O/P : ValueError    
                     #as the values are store of different datatype and "numpy array" only support one type of data

#NumPy Creating Arrays
arr = [1,2,3,4]
np_arr = np.array(arr)
print(type(np_arr))
print(np_arr) 

arr_1 = np.arange(10)
print(arr_1) # O/P : [0 1 2 3 4 5 6 7 8 9]

arr = np.arange(-4, 10, 2)
print(arr)     #    [-4 -2  0  2  4  6  8]

arr = np.random.rand(3,3)
print(f"matrix with random number of shape 3 x 3 : \n{arr}")

arr = np.random.randint(1,10,(3,3))
print(f"matrix with random number between 1 to 10 of shape 3 x 3 : \n{arr}")
#========================================================
#Indexing and Slicing :
arr = [1,2,3,4,9,0,6,2,76,90,23,65]
np_arr = np.array(arr)
print(np_arr[2])
print(np_arr[3:7])


#========================================================
#Dimensions and shape in Numpy Array
arr = [0 , 1,  2,  3, 4 ,5 ]
np_arr = np.array(arr)
print(np_arr.ndim) # 1
print(np_arr.dtype)

np_arr = np.array([[1,2,3], [5,6,7], [3,4,5]])
print(np_arr.ndim) 
print(np_arr.shape)
print(np_arr.size) 
#========================================================
#Reshaping of NumPy Array
arr_2 = [0 , 1,  2,  3, 4 ,5 ,6, 7, 8, 9]
np_arr = np.array(arr_2)
print(np_arr.reshape((2,5)))  #print(np_arr.reshape((5,2)))

np_arr = np.array([[1,2,3,4,5], [10,3,5,6,7], [8,0,3,4,5]])
#print(np_arr.shape)
print(np_arr.reshape(5,3))

np_arr = np.array([[1,2,3,4], [10,3,5,6,7], [8,0,3,4,5]])
print(np_arr.reshape(5,3)) # O/P : Error 

np_arr = np.array([[1,2,3], [5,6,7], [3,4,5]])
print(np_arr.reshape(-1)) # [1,2,3,5,6,7,3,4,5] --> Flatten the array
#print(np_arr.flatten())

np_arr = np.array([1,2,4,3,5,6,7,8,9,10,11,12])
print(np_arr.reshape(2,3,2))
#========================================================
#Sorting
np_arr = np.array([1,2,4,3,5,6,7,8,9,10,11,12])
print(np.sort(np_arr))
#Searching : 
np_arr = np.array([1,2,6,4,9,3,5,5,8,4,10])
print(np.where(np_arr == 5))
#========================================================
############Concatenate Array############
#========================================================
arr_1 = np.array([1,2,3,4,5])
arr_2 = np.array([10,3,5,6,7])
print(np.concatenate( (arr_1, arr_2) ) )

arr_1 = np.array( [ [1,2,3] ]) 
arr_2 = np.array( [ [0,6,7] ] ) 
print(np.concatenate( (arr_1, arr_2), axis = 0 ) ) #axis = 0 --> vertical 
# O/p :
#  [ [1 2 3]
#    [0 6 7] ] 

arr_1 = np.array( 
                [ [1,2,3],
                  [0,6,7] 
            ])  # shape (2, 3)
arr_2 = np.array( [ [4,5,6] ] )         # shape (1, 3)
print(np.concatenate( (arr_1, arr_2), axis = 0 ) ) 
# O/p : 
#[ [1 2 3]
#  [0 6 7]
#  [4 5 6] ]

arr_1 = np.array( [ [1,2,3] ]).reshape(3,1)  
arr_2 = np.array( [ [4,5,6] ] ).reshape(3,1)      
print(np.concatenate( (arr_1, arr_2), axis = 1 ) ) # axis = 1 --> horizontal
# O/P : 
#  [ [1 4]
#    [2 5]
#    [3 6] ]