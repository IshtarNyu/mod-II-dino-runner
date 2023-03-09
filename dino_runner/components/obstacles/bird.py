
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    
    def __init__(self,image):
        super().__init__(image)
        self.rect.y = 250
        self.index= 0
        
    def update(self,game_speed,obstacles):
        self.image = BIRD[0]  if self.index<=4  else BIRD[1]
        super().update(game_speed,obstacles)
        self.index +=1
        if self.index==8:
            self.index = 0
        
        
            
    
        