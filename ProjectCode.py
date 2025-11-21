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

class Player:

    def __init__(self):

        self.rect = pygame.Rect(screen_w // 2 - 25, screen_h - 50, 50, 40)



    def move(self, keys):

        if keys[pygame.K_LEFT] and self.rect.left > 0:

            self.rect.x -= play_s

        if keys[pygame.K_RIGHT] and self.rect.right < screen_w:

            self.rect.x += play_s

class Bullet:

    def __init__(self, x, y):

        self.rect = pygame.Rect(x - 2, y - 10, 5, 10)



    def update(self):

        self.rect.y -= bullet_s



    def off_screen(self):

        return self.rect.top < 0

class Enemy:

    def __init__(self, x, y):

        self.rect = pygame.Rect(x, y, 50, 40)



    def update(self):

        self.rect.y += enemy_s



    def off_screen(self):

        return self.rect.top > screen_h
