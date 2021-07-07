
from show import ShowAction

import numpy as np



arr = np.zeros((8,8), dtype='int')
arr[3,3] = -1
arr[4,4] = 1
arr[3,4] = -1
arr[4,3] = -1

arr[5,5] = -1
arr[6,6] = -1


obj = ShowAction(arr, -1)

print(obj.listactions())

print(arr)