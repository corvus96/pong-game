import pygame
import random

class Ball:
    def __init__(self, pos : tuple, width, height) -> None:
        self.ball_rect = pygame.Rect(pos[0], pos[1], width, height)
        # determine the x and y speed of the ball (0.1 is just to scale the speed down)
        self.accel_x = random.randint(2, 4) * 0.1
        self.accel_y = random.randint(2, 4) * 0.1
        
        # randomize the direction of the ball
        if random.randint(1, 2) == 1:
          self.accel_x *= -1
        if random.randint(1, 2) == 1:
          self.accel_y *= -1

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.ball_rect)

    def check_if_out_x_bounds(self, screen_width):
        if self.ball_rect.left <= 0 or self.ball_rect.left >= screen_width: 
            self.ball_rect.left = screen_width /2

    def check_if_out_y_bounds(self, screen_height):
        if self.ball_rect.top < 0:
          # invert its vertical velocity
          self.accel_y *= -1
        # do the same thing with the bottom
        if self.ball_rect.bottom > screen_height - self.ball_rect.height:
          self.accel_y *= -1
          
    
    def move(self, delta):
        self.ball_rect.left += self.accel_x * delta
        self.ball_rect.top += self.accel_y * delta
