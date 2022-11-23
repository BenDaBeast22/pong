from constants import *

def draw(win, paddles, ball, left_score, right_score):
  win.fill(BLACK)

  left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
  right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
  win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
  win.blit(right_score_text, (3*WIDTH//4 - right_score_text.get_width()//2, 20))

  for paddle in paddles:
    paddle.draw(win)
  
  DASH_WIDTH = 10
  for i in range(10, HEIGHT, HEIGHT//20):
    if i % 2 == 0:
      pygame.draw.rect(win, WHITE, (WIDTH//2 - DASH_WIDTH//2, i + 2.5, DASH_WIDTH, HEIGHT//20))
  
  ball.draw(win)
  
  pygame.display.update()

def handle_paddle_movement(keys, left_paddle, right_paddle):
  if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
    left_paddle.move(UP)
  if keys[pygame.K_s] and left_paddle.y + left_paddle.height + left_paddle.VEL <= HEIGHT:
    left_paddle.move(DOWN)

  if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
    right_paddle.move(UP)
  if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.height + right_paddle.VEL <= HEIGHT:
    right_paddle.move(DOWN)

def handle_collision(ball, left_paddle, right_paddle):
  # Ceiling and Floor Collisions
  if ball.y - ball.radius <= 0 or ball.y + ball.radius >= HEIGHT:
    ball.y_vel *= -1
    pygame.mixer.Sound.play(boop3)

  # Check Left Paddle Collision
  if ball.x_vel < 0:
    if ball.y > left_paddle.y and ball.y < left_paddle.y + left_paddle.height:
      if ball.x - ball.radius < left_paddle.x + left_paddle.width:
        middle_y = left_paddle.y + left_paddle.height/2 # center of paddle
        diff_y = ball.y - middle_y # dif between ball and center of paddle
        r_factor = (left_paddle.height / 2) / ball.MAX_VEL
        y_vel = diff_y / r_factor
        ball.y_vel = y_vel
        ball.x_vel *= -1
        pygame.mixer.Sound.play(boop)

  # Check Right Paddle Collision
  else:
    if ball.y > right_paddle.y and ball.y < right_paddle.y + right_paddle.height:
      if ball.x + ball.radius > right_paddle.x:
        middle_y = right_paddle.y + right_paddle.height/2 # center of paddle
        diff_y = ball.y - middle_y # dif between ball and center of paddle
        r_factor = (right_paddle.height / 2) / ball.MAX_VEL
        y_vel = diff_y / r_factor
        ball.y_vel = y_vel
        ball.x_vel *= -1 
        pygame.mixer.Sound.play(boop2)

def handle_score(ball, left_paddle, right_paddle, left_score, right_score):
    if ball.x + ball.radius > WIDTH + ball.radius * 3:
      left_score += 1
      ball.reset()
      left_paddle.reset()
      right_paddle.reset()

    if ball.x - ball.radius < 0 - ball.radius * 3:
      right_score += 1
      ball.reset()
      left_paddle.reset()
      right_paddle.reset()

