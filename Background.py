import pygame
from pygame import *

class background():
    def __init__(self, window, image, section_x = 0, section_y = 1280, section_width = 640, section_height = 640):
      """__init__ initializes the background image, scales the image to the size of the window, and highlights a section of that image

      Args:
          window (_type_): the pygame display
          image (_type_): the background image being imported
          section_x (int, optional): the x position of the image section. Defaults to 0.
          section_y (int, optional): the y position of the image section. Defaults to 1280.
          section_width (int, optional): the width of the section. Defaults to 640.
          section_height (int, optional): the height of the section. Defaults to 640.
      """
      self._window = window
      # Create the image
      self._image = pygame.image.load(image)
      self._image = pygame.transform.smoothscale(self._image, (640, 1280))
      self._rect = self._image.get_rect()

      # Define the section to draw
      self.section_x = section_x
      self.section_y = section_y
      self.section_width = section_width
      self.section_height = section_height
      self.section_rect = pygame.Rect(self.section_x, self.section_y, self.section_width, self.section_height)

    def draw(self):
        """Creates a rectangular section, and uses that section to create a subsurface of the initial image surface
        _window.blit creates the subsurface on the screen.
        """
        #Recreate the subsurface
        self.section_rect = pygame.Rect(self.section_x, self.section_y, self.section_width, self.section_height)
        # Create the subsurface
        self.section_image = self._image.subsurface(self.section_rect)
        self._window.blit(self.section_image, (self.section_x,self.section_y))
