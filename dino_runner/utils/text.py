
import pygame

from dino_runner.utils.constants import RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH
FONT_STYLE= 'freesansbold.ttf'
BlACK_COLOR = (0,0,0)

def get_score_element(points):
    font= pygame.font.Font(FONT_STYLE,20)
    text= font.render(f"Points:{points}", True,BlACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center= (1000,40)
    return text, text_rect

def get_centered_message(message):
    font=pygame.font.Font(FONT_STYLE,50)
    text= font.render(message, True,BlACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center= (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)    
    return text, text_rect


def get_centered_message2 (message):
    font=pygame.font.Font(FONT_STYLE,40)
    text= font.render(message, True,BlACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center= (SCREEN_WIDTH//2, SCREEN_HEIGHT//2-180)    
    return text, text_rect




def score_final(points):
    
    font= pygame.font.Font(FONT_STYLE,30)
    score =  font.render('Your score:' + str(points),True,BlACK_COLOR )
    score_rect = score.get_rect()

    score_rect.center= (SCREEN_WIDTH// 2 , SCREEN_HEIGHT// 2 +1000 )
    return score, score_rect


    
def get_deaths(death_count):
    
    font= pygame.font.Font(FONT_STYLE,20)
    text= font.render(f'Deaths: '+ str(death_count), True, BlACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center= (SCREEN_WIDTH// 2 , SCREEN_HEIGHT// 2 + 170 )
    
    return text, text_rect    

  

    
