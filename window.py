import pygame

class Window:
    """ Creates a window for a pygame 

    Attributes:
        screen: a window instance.
    Args: 
        screen_width:  constant for the window width value.
        screen_height:  constant for the window height value.
        title: set the window's title.
    """
    def __init__(self, screen_width : int, screen_height : int, title="") -> None:
         # initialize the PyGame library (this is absolutely necessary)
          pygame.init()

          # this creates the window for the game
          self.screen = pygame.display.set_mode((screen_width, screen_height))

          # set the window's title
          pygame.display.set_caption(title)

    def fill(self, color : tuple) -> None:
        """ fill with a color the game window.
        
        Args: 
            color: (R, G, B) where each channel can be from 0 to 255.
        """
        self.screen.fill(color)



