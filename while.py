# i = 0
# while i < 6:
#     print(i)
#     i += 1

# i = 0
# data = [2,4,6,8,10]
# sum = 0

# while i < len(data):
#     sum += data[i]
#     i += 1 

# rata_rata = sum/len(data)
# print(f'rata-rata : {rata_rata}')

# i = 0 
# data = [5,12,8,20,7,14,11]
# filtered_data = []

# while i < len(data):
#     if data[i] > 10:
#         filtered_data.append(data[i])
#     i += 1

# print(f'data yang sudah di filter : {filtered_data}')\
# 10, setalah angka 50 

# data = [1,2,3]
# data.insert(0,10)
# data.insert(3,50)
# data[4] = 100

# print(data)

import array as arr
a = arr.array('i',[1,2])

import numpy as np
array = np.array([['a','b','c'],[1,2,3],['x','y','z']])
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
gabunganVertical = np.vstack((array1,array2))
gabunganHorizontal = np.hstack((array1,array2))
gabunganConcat = np.concatenate((array1,array2),axis=0)
# print(gabunganConcat[1:3])
# # print(gabunganVertical)
# print(gabunganHorizontal)

print(array[:,0])