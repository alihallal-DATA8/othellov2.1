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
      
        poss_list = []
        for point in op_pos:
            for add_x , add_y in set([*permutations([-1,1,0, 1, -1],2)]):
                x = point[0] + add_x
                y = point[1] + add_y
                if  x <8 and x>=0 and y < 8 and y >=0:
                    if self.arr[x,y] == 0:

                        poss_list.append((x,y))
       
       

    #    occupied_pos = self.total_occupied()
       
       
    #    return set(poss_list).difference(occupied_pos)  

        return poss_list


        


