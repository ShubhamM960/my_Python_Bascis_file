import numpy as np
np_arr = np.array( [ 
                   [1,6,3],
                   [8,4,0]
                ]) 
print(f" elements have more than 4:  { np_arr > 4  }")
print(f" show elements have more than 4:  { np_arr[ np_arr > 4 ] }")