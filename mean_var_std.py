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
    
    axstd_1 = mvs_array.std(axis=0)
    axstd_2 = mvs_array.std(axis=1)
    array_std = mvs_array.std()
    
    axmax_1 = mvs_array.max(axis=0)
    axmax_2 = mvs_array.max(axis=1)
    array_max = mvs_array.max()
    
    axmin_1 = mvs_array.min(axis=0)
    axmin_2 = mvs_array.min(axis=1)
    array_min = mvs_array.max()
    
    axsum_1 = mvs_array.sum(axis=0)
    axsum_2 = mvs_array.sum(axis=1)
    array_sum = mvs_array.sum()
        
    dic = {
        'mean': [axmean_1.tolist(), axmean_2.tolist(), float(array_mean)],
        'Variance': [axvar_1.tolist(), axvar_2.tolist(), float(array_var)],
        'Standar deviation': [axstd_1.tolist(), axstd_2.tolist(), float(array_std)],
        'Max': [axmax_1.tolist(), axmax_2.tolist(), float(array_max)],
        'Min': [axmin_1.tolist(), axmin_2.tolist(), float(array_min)],
        'Sum': [axsum_1.tolist(), axsum_2.tolist(), float(array_sum)]             
    }
    
    return dic

dic = calculate(mvs_array)
print(dic)

