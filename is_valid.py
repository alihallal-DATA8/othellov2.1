

from possbilities import Possibilities

class IsValid():
    def __init__(self,arr , pos, color):
        self.arr = arr
        self.pos = pos
        self.color = color

    def occuppied(self):
        x , y = self.pos
        return self.arr[x,y] == 0

    def check_proximity(self):
        x , y = self.pos
        set_of_proximity = Possibilities(self.arr, self.color).proximity()
    #    print(x,y)
    #    print(set_of_proximity)
        return ((x,y) in set_of_proximity)
        
    