import pygame

class Player:
    def __init__(self, left_top_position : tuple, width : int, height : int) -> None:
        self.paddle = pygame.rect.Rect(left_top_position[0], left_top_position[1], width, height)
        self.move = 0
        self.score = 0

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.paddle)

    def collision(self, ball):
        if self.paddle.colliderect(ball.ball_rect) and self.paddle.left < ball.ball_rect.left:
          ball.accel_x *= -1
          ball.ball_rect.left += 5

        if self.paddle.colliderect(ball.ball_rect) and self.paddle.left > ball.ball_rect.left:
          ball.accel_x *= -1
          ball.ball_rect.left -= 5

    def check_bounds(self, screen_height):
       if self.paddle.top < 0: self.paddle.top = 0
       if self.paddle.bottom > screen_height: self.paddle.bottom = screen_height

    def move_paddle(self, delta):
        self.paddle.top += self.move * delta