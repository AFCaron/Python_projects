#coin flip simulator

import random

class Coin():
    def __init__(self):
        self.faces = ['head','tail']
        self.stat_head = 0
        self.stat_tail = 0
        
    def flip(self):
        self.result = random.sample(self.faces, 1)[0]
        print(f"the result of the toss is {c.result}")
        
    def throw_stat(self):
        
        if self.result == 'head':
            self.stat_head += 1
            
        elif self.result == 'tail':
            self.stat_tail += 1
            
        print(f"number of heads {c.stat_head}\nnumber of tails {c.stat_tail}")    
        
        
        

game = 'y'
c = Coin()
while game == 'y':
    game = input('play y/n?')
    
    c.flip()
    c.throw_stat()
    
    print(f"number of heads {c.stat_head}\nnumber of tails {c.stat_tail}")
    
