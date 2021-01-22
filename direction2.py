import numpy as np
from possbilities import Possibilities
from itertools import permutations


class  Direction(Possibilities):
    def __init__(self, arr, pos, color):
        self.arr = arr
        self.pos = pos
        self.color = color

    

    def current_proximity(self):

        op_pos = self.get_oponent_position()
        poss_dirc = []
        x_cen,y_cen = self.pos
        for add_x , add_y in set([*permutations([-1,1,0, 1, -1],2)]):
            x = x_cen + add_x
            y = y_cen + add_y
            if  x <8 and x>=0 and y < 8 and y >=0:
                if self.arr[x,y] == -self.color:
                    poss_dirc.append((add_x,add_y))
    
        return poss_dirc

    def check_friend(self):
        arr_copy2 = self.arr.copy()
        poss_dirc = self.current_proximity()
        

        if len(poss_dirc) ==0:
            return  arr_copy2, False

        
        else:
            poss = []    
            x , y = self.pos
            #x_1st, y_1st = x + add_x , y + add_y
            arr_copy = self.arr.copy()
            arr_copy[x,y] = self.color
            for add_x, add_y in poss_dirc:
                #arr_copy[x_1st,y_1st] = self.color
                temp_copy = arr_copy.copy()

                x_next , y_next = x + add_x , y + add_y 
                temp_copy[x_next,y_next] = self.color
                #check continuty 
                cond = (x_next >= 0) and (y_next >=0) and (x_next < 8) and (y_next < 8 )

                #arr_copy[x_next,y_next] = self.color

                while  cond and (self.arr[x_next, y_next] == -self.color):
                    #pos = (x_next, y_next)

                    temp_copy[x_next,y_next] = self.color

                    x_next , y_next = x_next + add_x , y_next + add_y
                    cond = (x_next >= 0) and (y_next >=0) and (x_next < 8) and (y_next < 8 )

                    print(x_next, y_next, cond)
                    if not cond:
                        break
                
                if x_next < 0:
                    x_next += 1
                if x_next > 7:
                    x_next -= 1
                
                if y_next < 0:
                    y_next += 1
                if y_next > 7:
                    y_next -= 1
                
                    

                if self.arr[x_next, y_next] == self.color:
                    arr_copy = temp_copy.copy()

                    poss.append((arr_copy, True))

                
                else: 

                    poss.append((arr_copy2, False))
                
        nb_poss = 0
        for arr, cond in poss[::-1]:
            if cond:
                nb_poss += 1
                return arr, True

        return arr_copy2, False


        