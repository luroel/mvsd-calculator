import numpy as np

list = ([0,1,2,3,4,5,6,7,8])
mvs_array = np.array([list]).reshape(3,3)

def calculate(mvs_array):
    axmean_1 = mvs_array.mean(axis=0) #mean rows
    axmean_2 = mvs_array.mean(axis=1) #mean colums
    array_mean = mvs_array.mean()
    
    axvar_1 = mvs_array.var(axis=0)
    axvar_2 = mvs_array.var(axis=1)
    array_var = mvs_array.var()
    
    
    
    dic = {
        'mean': [axmean_1.tolist(), axmean_2.tolist(), float(array_mean)],
        'Variance': [axvar_1.tolist(), axvar_2.tolist(), float(array_var)],
        'Standar deviation': [],
        'Max': [],
        'Min': [],
        'Sum': []             
    }
    
    return dic

dic = calculate(mvs_array)
print(dic)

