

import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.large_cactus import LargeCactus
from dino_runner.components.obstacles.stego import Stego

from dino_runner.utils.constants import BIRD, DEAD, HAMMER_TYPE, LARGE_CACTUS, SHIELD_TYPE, SMALL_CACTUS, STEGO


class ObstacleManager():
    def __init__(self):
        self.obstacles=[]
        
    def generate_obstacle(self):
        obstac_types = {
            
            0: Cactus(SMALL_CACTUS[0]),
            1: Cactus(SMALL_CACTUS[1]),
            2: Cactus(SMALL_CACTUS[2]),
            3: LargeCactus(LARGE_CACTUS[0]),
            4: LargeCactus(LARGE_CACTUS[1]),
            5: LargeCactus(LARGE_CACTUS[2]),
            6: Bird(BIRD[0]),
            7: Stego(STEGO[0])
            
        }
        return obstac_types [random.randint(0,7)]
                
            
    def update(self,game):
        if len(self.obstacles) == 0:
            self.obstacles.append(self.generate_obstacle())
            
                

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            
            
            if game.player.type == SHIELD_TYPE:
                print("Shielf activate,no damege")
                
            elif game.player.type == HAMMER_TYPE and game.player.dino_rect.colliderect(obstacle.rect):
                
                self.obstacles.pop()
                
                


                print("hammer activate,no damege")    
    
                
            elif game.player.dino_rect.colliderect(obstacle.rect):
                
                game.player.image = DEAD
                
                game.playing= False
                break
        
    def draw(self,screen):
        
        for obstacle in self.obstacles:
            
            obstacle.draw(screen)
            
    def remove_obstacles(self):
        self.obstacles=[]
        
    def remove_power_ups(self):
        self.power_ups=[]    

          
            
       
        
            
            