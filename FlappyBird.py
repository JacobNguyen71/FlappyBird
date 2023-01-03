import pygame
import neat
import time
import os
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
BIRD_IMGS = []
for i in range(3):
    bird_img = pygame.image.load(f'imgs/bird{i}.png').convert_alpha
    bird_img = pygame.transform.scale2x
    BIRD_IMGS.append(bird_img)
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))