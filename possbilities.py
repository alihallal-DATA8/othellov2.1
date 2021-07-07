from itertools import permutations
import numpy as np

class Possibilities:
    def __init__(self, arr, color):
        self.arr = arr
        self.color = color
    

    def get_position(self):
        x_cur, y_cur = np.where(self.arr == -self.color)
        cur_pos = [*zip(x_cur, y_cur)]
        return cur_pos

    def get_oponent_position(self):
        x_op , y_op = np.where(self.arr == self.color)
        op_pos = [*zip(x_op, y_op)]
        return op_pos
   
    def total_occupied(self):
        return self.get_oponent_position() + self.get_position()

    def proximity(self):
        #cur_pos = self.get_position()
        op_pos  = self.get_oponent_position()
        #print(op_pos)
        poss_list = []
        for x_op , y_op in op_pos:

            #print(len(op_pos))
            for add_x , add_y in set([*permutations([-1,1,0, 1, -1],2)]):
                x1 = x_op + add_x
                y1 = y_op + add_y
                if  x1 <8 and x1>=0 and y1 < 8 and y1 >=0:
                    if self.arr[x1,y1] == 0:
                        #print(x1,y1)
                        poss_list.append((x1,y1))
       
        return poss_list


        


