import configparser, pygame, time, socket, threading
from pygame.locals import *


config = configparser.ConfigParser()
address = ('<broadcast>', 54545)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
hostname = socket.gethostname()
pygame.init()

# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("In With Us?")
time.sleep(10)

