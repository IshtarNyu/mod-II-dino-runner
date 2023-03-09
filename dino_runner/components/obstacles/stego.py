

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, STEGO


class Stego(Obstacle):
    
    def __init__(self,image):
        super().__init__(image)
        self.rect.y = 325
        self.index= 0
        
    def update(self,game_speed,obstacles):
        self.image = STEGO[0]  if self.index<=4  else STEGO[1]
        super().update(game_speed,obstacles)
        self.index +=1
        if self.index==8:
            self.index = 0
        
        
            
    
        