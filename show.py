from direction2 import Direction

class ShowAction:

    def __init__(self,arr,color):
        self.arr = arr
        self.color = color

    def listactions(self, loun1, loun2):

        dirc = Direction(self.arr, (0,0), loun1)
        
        actions = []
        for poss in dirc.proximity():
            dirc2 = Direction(self.arr, poss, loun2)

            _, whatisit = dirc2.check_friend()
            if whatisit:
                actions.append(poss)
        
        return set(actions)


