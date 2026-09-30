#call by value applicable on immutatable data types 
    #like string, int, float
    
def modify_value( x) -> int:
    x= x+5
    return x

v = 23
print(f"value before mutating is : {v} ")
updatevalue  = modify_value(v)
print(f"updated value is : {updatevalue} ")

#===================================================================
#===================================================================
#call by reference applicable on mutable data types 
    #like list, dict
    
def modify_lst( my_lst) -> None:
    my_lst.append('new value')

original_lst = [2, 4, 'value1', {'key1' : 'value1'}]
print(f"dictionary value before mutating is : {original_lst} ")
modify_lst(original_lst)
print(f"dictionary value before mutating is : {original_lst} ")

# o/p : 
# dictionary value before mutating is : [2, 4, 'value1', {'key1': 'value1'}] 
# dictionary value before mutating is : [2, 4, 'value1', {'key1': 'value1'}, 'new value'] 


def modify_dict( my_dict):
    my_dict['key2'] = 'new value'

original_dict = {'key1' : 'value1'}
print(f"dictionary value before mutating is : {original_dict} ")
modify_dict(original_dict)
print(f"dictionary value before mutating is : {original_dict} ")

# o/p :
# dictionary value before mutating is : {'key1': 'value1'} 
# dictionary value before mutating is : {'key1': 'value1', 'key2': 'new value'} 