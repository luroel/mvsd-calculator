import numpy as np

list = ([0,1,2,3,4,5,6,7,8])
mvs_array = np.array([list]).reshape(3,3)

def calculate(mvs_array):
    mvs_array = np.array([list]).reshape(3,3)
    axis_1 = mvs_array.mean(axis=0) #mean rows
    axis_2 = mvs_array.mean(axis=1) #mean colums
    flatten = mvs_array.mean()
    
    return print(axis_1, axis_2, flatten)

calculate(mvs_array)

