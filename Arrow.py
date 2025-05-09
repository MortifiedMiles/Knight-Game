import pygame
from pygame import *
import random

class arrow():
    def __init__(self, window, image = 'Images/Arrow.png', y_speed = 2, scale_factor = 1):
        """__init__ initializes the arrow objects, the size of the image, the size of the hitbox,
        and variables referenced later within the class.

        Args:
            window (_type_): pygame display
            image (str, optional): the arrow image. Defaults to 'Images/Arrow.png'.
            y_speed (int, optional): the vertical arrow movement speed. Defaults to 2.
            scale_factor (int, optional): an int which can be used to scale the size of the image. Defaults to 1.
        """
        # Initialize Image and Rectangle
        self.scale_factor = scale_factor
        self._image = pygame.image.load(image)
        self._image = pygame.transform.scale_by(self._image, self.scale_factor)
        self._rect = self._image.get_rect()
        self._rect.width = 10
        
        # Pick a random starting position
        self._rect.x = random.randint(128, 388)
        self._rect.y = window.get_height() - 100

        # Initialize Other Variables:
        self._y_speed = y_speed
        self.__window = window

                
    @property
    def rect(self):
        """shows the rect property

        Returns:
            _type_: rectangle dimensions
        """
        return self._rect
    
    @property
    def pos(self):
        """shows the arrow position

        Returns:
            int: arrow position (x,y)
        """
        return (self._rect.x, self._rect.y)
    
    @property
    def x(self):
        """shows the x position of the arrow

        Returns:
            int: arrow position (x)
        """
        return self._rect.x
    
    @property
    def y(self):
        """shows the y position of the arrow

        Returns:
            int: arrow position (y)
        """
        return self._rect.y
    
    @x.setter
    def x(self, new_x):
        """sets a new x position for the arrow

        Args:
            new_x (int): new arrow position (x)
        """
        self._rect.x = new_x
        
    @y.setter
    def y(self, new_y):
        """sets a new y position for the arrow

        Args:
            new_y (int): new arrow position (y)
        """
        if 0 - self._rect.height <= new_y < self.window.get_height():
            self._rect.y = new_y
    
    @property
    def y_speed(self):
        """shows the vertical movement speed of the arrow

        Returns:
            int: vertical arrow movement speed(_x_speed)
        """
        return self._y_speed
    
    @y_speed.setter
    def y_speed(self, new_speed):
        """sets a new movement speed for the arrow

        Args:
            new_speed (int): new arrow vertical movement speed(new_speed)
        """
        self._y_speed = new_speed
    
    @property
    def window(self):
        """shows the pygame display which the arrow will be used in

        Returns:
            _type_: pygame display
        """
        return self.__window
    
    def continuous_move(self):
        """if the position of the arrow will not dissappear on the top or bottom of the screen, then the
        arrows y position decreases by the y_speed
        """
        if (self.y >= 0 - self._rect.height) or (self.y <= self._window.get_height() + self._rect.height):
            self.y -= self.y_speed
        pass
    
    def draw(self):
        """draws the image on the window using the (x,y) position
        """
        self.__window.blit(self._image, self.pos)
