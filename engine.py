from board import Board
from is_valid import IsValid
from direction2 import Direction
from possbilities import Possibilities
from itertools import permutations
from show import ShowAction

import time
import numpy as np
import matplotlib.pyplot as plt

class Engine(Board):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
    def play(self):
        nb =  0
        color = -1
        c_op = 'white'
        
        fig = self.createboard()
        while True:
            pts = []
            


            actions = ShowAction(self.arr, color)

            set_of_actions = actions.listactions(color, -color)

            x_poss = [a for a,_ in set_of_actions]
            y_poss = [b for _,b in set_of_actions]

            #ac = plt.plot(x_poss, y_poss, 'blue', lw ='0', marker = '*', markersize=5, alpha = 0.5)
            
            if len(set_of_actions) == 0:
                
                print('skip me')
                pts = 'skip'
                nb+=1


            if c_op == 'black' and len(set_of_actions) !=0:
                list_of_actions = list(set_of_actions)
                index_random = np.random.choice(len(list_of_actions),1)[0]
                pts = list_of_actions[index_random]
 
            while len(pts) < 1 :
 

                pts = plt.ginput(1, timeout=-1)[0]
                pts = np.round(pts).astype(int)
                x,y = pts
                ######block valid####
                direc = Direction(self.arr, pts, -color)

                _, cond1 = direc.check_friend()

                occuppied = self.arr[x,y] != 0


                while ( occuppied) or  (not cond1) :
                    self.message = f' This is not a valid move:\n{c_op.capitalize()} its your turn, try again'
                    self.tellme()
                    pts = plt.ginput(1, timeout=-1)[0]
                    pts = np.round(pts).astype(int)
                    x,y = pts
                    occuppied = self.arr[x,y] != 0

                    cond = IsValid(self.arr,pts, -color)
                    direc = Direction(self.arr, pts, -color)
                    
                    _, cond1 = direc.check_friend()



                ######block direc######

            direc = Direction(self.arr, pts, -color)

            if pts != "skip":
                self.arr, _ = direc.check_friend()         
          

            if nb % 2 == 0:

                color =  1
                c_op = 'black'
            else :
                color =  -1
                c_op = 'white'

            nb +=1
            print(nb)

            self.message = f'it is {c_op.capitalize()} turn,  choose a cell'
            self.tellme()
   
#            plt.pause(5)
            
            w_x, w_y  = np.where(self.arr == 1)
            b_x, b_y  = np.where(self.arr == -1)

            ph = plt.plot(w_x, w_y, 'gray', lw ='0', marker = 'o', markersize=20, alpha = 1)
            ph = plt.plot(b_x, b_y, 'k', lw ='0', marker = 'o', markersize=20)
            #plt.close()
            
            #plt.show()
            
            #plt.close()


