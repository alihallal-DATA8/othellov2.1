from engine import Engine
import numpy as np



arr = np.zeros((8,8), dtype='int')
arr[3,3] = 1
arr[4,4] = 1
arr[3,4] = -1
arr[4,3] = -1

arr[5,5] = 1
arr[6,6] = -1


#print(arr)

#test = IsValid(arr, (3,4))

#print(test.proximity())

test = Engine( )

test.play()
#print(arr)
#test = Direction(arr, (3,1), -1)
#print(test.current_proximity())

#cond , arr = test.check_friend()

#print(cond)

#arr[3,5] = 1

