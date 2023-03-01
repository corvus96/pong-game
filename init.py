from window import Window
from player import Player
from ball import Ball
import pygame

# constants for the windows width and height values
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

# the RGB values for the colors used in the game
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

def main():
    wd = Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Pong")
    player_1 = Player((30, 0), 7, 100)
    player_2 = Player((SCREEN_WIDTH - 50, 0), 7, 100)
    ball = Ball((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 25, 25)
    player_1.draw(wd.screen, COLOR_WHITE)
    player_2.draw(wd.screen, COLOR_WHITE)
    ball.draw(wd.screen, COLOR_WHITE)

    # create the clock object to keep track of the time
    clock = pygame.time.Clock()

    """
    this is to check wheter or not to move the ball
    we will make it move after 3 seconds
    """
    started = False

    while True:
        wd.fill(COLOR_BLACK)

        # make the ball move after 3 seconds
        if not started:
          # load the Consolas font
          font = pygame.font.SysFont('Consolas', 30)

          # draw some text to the center of the screen
          text = font.render('Press Space to Start', True, COLOR_WHITE)
          text_rect = text.get_rect()
          text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
          wd.screen.blit(text, text_rect)

          # update the display
          pygame.display.flip()

          clock.tick(60)

          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              return
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE:
                started = True

          continue

        '''
        get the time elapse between now and the last frame
        60 is an arbitrary number but the game runs smooth at 60 FPS
        '''
        delta_time = clock.tick(60)

        # checking for events
        for event in pygame.event.get():

            # if the user exits the window
            if event.type == pygame.QUIT:
                # exit the function, to finish the game
                return

            # if the user is pressing a key
            if event.type == pygame.KEYDOWN:
                # PLAYER 1
                # if the key is W, set the movement of paddle_1 to go up
                if event.key == pygame.K_w: player_1.move = -0.5

                # if the key is S, set the movement of paddle_1 to go down
                if event.key == pygame.K_s: player_1.move = 0.5

                # PLAYER 2
                # if the key is the up arrow, set the movement of paddle_2 to go up
                if event.key == pygame.K_UP: player_2.move = -0.5
                # if the key is the down arrow, set the movement of paddle_2 to go down
                if event.key == pygame.K_DOWN: player_2.move = 0.5

            # if the player released a key
            if event.type == pygame.KEYUP:
                # if the key released is w or s, stop the movement of player_1
                if event.key == pygame.K_w or event.key == pygame.K_s: player_1.move = 0.0
                # if the key released is the up or down arrow, stop the movement of player_2
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN: player_2.move = 0.0

        # apply paddle movement
        player_1.move_paddle(delta_time)
        player_2.move_paddle(delta_time)
        # check ball and move it
        ball.check_if_out_x_bounds(SCREEN_WIDTH)
        ball.check_if_out_y_bounds(SCREEN_HEIGHT)
        if started: ball.move(delta_time)
        # check ball collision with paddles
        player_1.collision(ball)
        player_2.collision(ball)
        # check paddle collisions with bounds
        player_1.check_bounds(SCREEN_HEIGHT)
        player_2.check_bounds(SCREEN_HEIGHT)
        # draw
        ball.draw(wd.screen, COLOR_WHITE)
        player_1.draw(wd.screen, COLOR_WHITE)
        player_2.draw(wd.screen, COLOR_WHITE)
        # draw score
        font = pygame.font.SysFont('Consolas', 80)

        # draw some text to the center of the screen
        if ball.ball_rect.left <= 0: player_2.score += 1
        if ball.ball_rect.left >= SCREEN_WIDTH: player_1.score += 1
        text = font.render(str(player_1.score), True, COLOR_WHITE)
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 1.2)
        wd.screen.blit(text, text_rect)
        text = font.render(str(player_2.score), True, COLOR_WHITE)
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 1.2)
        wd.screen.blit(text, text_rect)
        # update the display (this is necessary for Pygame)
        pygame.display.update()



if __name__ == '__main__':
  main()
