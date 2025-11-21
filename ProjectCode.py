import pygame
import random



pygame.init()



screen_w = 800

screen_h = 600

fps = 60

play_s = 5

bullet_s = 7

enemy_s = 2

enemy_num = 10

w_score = 1000



wh = (255, 255, 255)

red = (255, 0, 0)


bl = (0, 0, 0)

gr = (0, 255, 0)

screen = pygame.display.set_mode((screen_w, screen_h))

pygame.display.set_caption("Galactica")

font = pygame.font.SysFont("Times New Roman", 24)

large_font = pygame.font.SysFont("Times New Roman", 48)
