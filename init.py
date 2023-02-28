from window import Window
import pygame
# constants for the windows width and height values
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

# the RGB values for the colors used in the game
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

def main():
    wd = Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Pong")

    while True:
        wd.fill(COLOR_BLACK)

        # checking for events
        for event in pygame.event.get():

          # if the user exits the window
          if event.type == pygame.QUIT:

            # exit the function, to finish the game
            return

if __name__ == '__main__':
  main()
