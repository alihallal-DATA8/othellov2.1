from board import Board
from is_valid import IsValid
from direction2 import Direction

import time
import numpy as np
import matplotlib.pyplot as plt

class Engine(Board):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.nb = nb
        #self.color = color
        
    def play(self):
        nb =  0
        color = -1
        c_op = 'red'
        self.createboard()
        while True:
            pts = []
            while len(pts) < 1 :
               
                pts = plt.ginput(1, timeout=-1)[0]
                pts = np.round(pts).astype(int)
            #    self.message = f'it is {color.capitalize()} turn,  choose a cell'
            #    self.tellme()
                x,y = pts
                #x = -my +7
                #y = mx
                ######block valid####
                cond = IsValid(self.arr,pts, -color)
                #print(color)
               # print(self.arr)
                direc = Direction(self.arr, pts, -color)

                _, cond1 = direc.check_friend()
                #print("diag:", cond1, direc.current_proximity())

                occuppied = self.arr[x,y] != 0
                #print('occ', occuppied)

                #print('check_prox', cond.check_proximity())               


                while ( occuppied) or  (not cond1) :
                    self.message = f' This is not a valid move:\n{c_op.capitalize()} its your turn, try again'
                    self.tellme()
                    pts = plt.ginput(1, timeout=-1)[0]
                    pts = np.round(pts).astype(int)
                    x,y = pts
                    occuppied = self.arr[x,y] != 0
                #    print(my,mx-7)
                #    x = -my +7
                #    y = mx
                    cond = IsValid(self.arr,pts, -color)
                    direc = Direction(self.arr, pts, -color)
                    
                    _, cond1 = direc.check_friend()
                    print("diag2:", cond1, direc.current_proximity())



                ######block direc######
            #print(color)
            direc = Direction(self.arr, pts, -color)

            self.arr, _ = direc.check_friend()
            

            if nb % 2 == 0:
                color =  1
                c_op = 'blue'
            #    self.arr[x,y] = 1
            else :
                color =  -1
                c_op = 'red'
            #    self.arr[x,y] = -1
            
           # print(np.flip(self.arr.T, axis=0))
           # print(x,y)

            self.message = f'it is {c_op.capitalize()} turn,  choose a cell'
            self.tellme()
   
    
            nb +=1

            r_x, r_y  = np.where(self.arr == 1)
            b_x, b_y  = np.where(self.arr == -1)


            ph = plt.plot(r_x, r_y, 'r', lw ='0', marker = 'o', markersize=20)
            ph = plt.plot(b_x, b_y, 'b', lw ='0', marker = 'o', markersize=20)

