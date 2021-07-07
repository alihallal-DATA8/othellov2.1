import time

import numpy as np
import matplotlib.pyplot as plt

class Board:
    def __init__(self, arr = np.zeros((8,8), dtype='int'), message = 'Welcome! TO Othello....White player Starts', **kwargs):
        self.arr =  arr 
        self.message = message
        
    def initialize(self):
        self.arr[3,3] = 1
        self.arr[4,4] = 1
        self.arr[3,4] = -1
        self.arr[4,3] = -1


    def count_score(self):
        wcount, _ = np.where(self.arr == 1) 
        bcount, _ = np.where(self.arr == -1)

        return wcount, bcount


    def tellme(self):
#        print(self.message)
        plt.xlabel(self.message, fontsize=10, color='white')
        wcount, bcount =  self.count_score()    
        plt.title(f"score \n White : {len(wcount)}  Black : {len(bcount)} ",  color='white')
        plt.draw()



    def createboard(self):
        
        plt.figure(figsize=(4,4), facecolor='green')
        plt.grid(True, which = 'major', lw = 2 , color = 'k')
        #plt.tick_params(axis ='both',which='minor')
        plt.xlim(-0.5,7.5)
        plt.xticks(np.arange(-0.5,8.5,1), labels=[])
        plt.ylim(-0.5,7.5)
        plt.yticks(np.arange(-0.5,8.5,1), labels=[])    
        self.initialize()
        self.tellme()
        w_x, w_y  = np.where(self.arr == 1)
        b_x, b_y  = np.where(self.arr == -1)
        
        ph = plt.plot(w_x, w_y, 'gray', lw ='0', marker = 'o', markersize=20, alpha = 1)
        ph = plt.plot(b_x, b_y, 'k', lw ='0', marker = 'o', markersize=20)
