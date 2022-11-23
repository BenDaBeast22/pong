import pygame
from constants import *
from classes import *
from functions import *
pygame.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

def main():
  run = True
  clock = pygame.time.Clock()

  left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
  right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
  ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)
  left_score = 0
  right_score = 0

  while run:
    clock.tick(FPS)
    left_paddle.draw(win)
    draw(win, [left_paddle, right_paddle], ball, left_score, right_score)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    keys = pygame.key.get_pressed()
    handle_paddle_movement(keys, left_paddle, right_paddle)
    
    ball.move()
    handle_collision(ball, left_paddle, right_paddle)

    if ball.x + ball.radius > WIDTH + ball.radius * 3:
      left_score += 1
      pygame.mixer.Sound.play(score)
      ball.reset()
      left_paddle.reset()
      right_paddle.reset()

    if ball.x - ball.radius < 0 - ball.radius * 3:
      right_score += 1
      pygame.mixer.Sound.play(score2)
      ball.reset()
      left_paddle.reset()
      right_paddle.reset()
      
    # handle_score(ball, left_paddle, right_paddle, left_score, right_score) 

  pygame.quit()

if __name__ == '__main__':
  main()


