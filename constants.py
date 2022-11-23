import pygame
import os
pygame.init()

# Constants
FPS = 60
WHITE = (255,255,255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 700, 500
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 8
UP = True
DOWN = False

# Pygame Constants
pong1 = os.path.join("")
SCORE_FONT = pygame.font.SysFont("comicsans", 50)
boop = pygame.mixer.Sound("sound_effects/pong.wav")
boop2 = pygame.mixer.Sound("sound_effects/pong2.wav")
boop3 = pygame.mixer.Sound("sound_effects/pong3.wav")
score = pygame.mixer.Sound("sound_effects/score.wav")
score2 = pygame.mixer.Sound("sound_effects/score2.wav")
