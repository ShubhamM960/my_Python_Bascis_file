#Broadcasting :
#   - NumPy’s ability to perform element-wise operations on arrays of different shapes.
#   - The smaller array is “broadcast” across the larger array so that they have compatible shapes. i.e. :
#           ~ if there is an Array 'A' having size 4*3 and array 'B' having size 1*3 then , 
#              numpy compares there size and store the same row value 4 times to have same shape size and 4*3 and
#              then start performing operation.
#           ~ if there is an Array 'A' having size 4*3 and array 'B' having size 4*1 then , 
#              numpy compares there size and store the same column value 3 times to have same shape size and 4*3 and
#              then start performing operation.


import numpy as np

np_arr_1 = np.array([1,2,3,4])
print('array after additon', np_arr_1 + 5) #[6,7,8,9]
print('array after additon', np_arr_1 * 5) #[5, 10, 15, 20]

arr_1 = np.array( [ [1,2,3],[0,6,7], [9,4,8] ])  # shape (3, 3)
arr_2 = np.array( [ [4,5,6] ] )                 # shape (1, 3)
print(arr_1 + arr_2)
# O/P : 
# [[ 5  7  9]
#  [ 4 11 13]
#  [13  9 14]]
np_arr_1 = np.array([1,2,3,4])
np_arr_2 = np.array([12, 24, 23, 47])
print('Element wise additon for arrays', np_arr_1 + np_arr_2) #[13 26 26 51]

arr_1 = np.array( [ [1,2,3],[0,6,7], [9,4,8], [2,4,1] ])  # shape (3, 3)
arr_2 = np.array( [ [4,5,6], [-2,5,6] ] )                 # shape (1, 3)
print(arr_1 + arr_2) 
# O/P : operands could not be broadcast together with shapes (4,3) (2,3)
#            ```As the broadcast show be between m*n and 1*n  or m*n and m*1

#===============================================================
#compute avg, median from the large set of data 
np_arr_1 = np.array([1,2,3,4, 59, 39, 56, 223, 15, 90, 58, 34])
np.median(np_arr_1)
np.mean(np_arr_1)
np.std(np_arr_1)
np.sum(np_arr_1)
#############################################
####### F I L T E R from numpy array ########
#############################################
np_arr = np.array([1,2,3,4, 59, 39, 56, 223, 15, 90, 58, 34])

print(np_arr > 10) # [False False False False  True  True  True  True  True  True  True  True]
#boolean mask
print( np_arr[ np_arr > 10 ] ) #[ 59  39  56 223  15  90  58  34]
    #mean / avg of number > 10
print('avg of number greater than 10 :', np_arr[np_arr > 10].mean()) # 71.5
    #multiple condition
print(np_arr[ (np_arr > 10) & (np_arr < 50) ]) #[39, 15, 34]
print(np_arr[ (np_arr > 10) | (np_arr < 50) ])

np_arr = np.array( [ 
                   [1,6,3],
                   [8,4,0]
                ]) 
print(f" check each elements which has  more than 4:  { np_arr > 4  }") 
print(f" show elements which has more than 4:  { np_arr[ np_arr > 4 ] }")
# #O/P : 
# # check each elements which has  more than 4: [[False  True False]
#                                                     [ True False False]]
# # show elements which has more than 4: [6 8]

np_arr = np.array( [ 
                   [1,2,3],
                   [0,6,7], 
                   [9,4,8], 
                   [2,4,1] 
                ]) 
print(f" 2th column which row element has more than 6:  {np_arr[ :, 2] > 6}") # O/P : [False  True  True False]
print(f"check only those rows with 2th column element greater than 6 : {np_arr[ np_arr[:, 2] > 6 ]}" )
# #O/P :
# [[0 6 7]
#  [9 4 8]]
