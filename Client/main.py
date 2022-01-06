import configparser, pygame, time
from pygame.locals import *


config = configparser.ConfigParser()
pygame.init()
# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("In With Us?")
button = pygame.image.load('cave.jpg')
button = pygame.transform.scale(button, (40, 60))
screen.blit(button, (0,0))
time.sleep(10)

