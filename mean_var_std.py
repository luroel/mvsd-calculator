import numpy as np

list = ([0,1,2,3,4,5,6,7,8])

def calculate(list):
    mvs_array = np.array([list])
    return print(mvs_array.reshape(3,3)) 

calculate(list)

