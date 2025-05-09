import pygame
import sys
from pygame import *

class simpleText():
    def __init__(self, window, text, x = 0, y = 0, font = 'Comic Sans MS',
                 fontSize = 50, color = (255, 255, 255)):
        """__init__ initializes the text font, the color, the window, the textsx and y position, the text itself, 
        and renders the text.

        Args:
            window (_type_): pygame display
            text (str): the text to be displayed
            x (int, optional): the x position of the text. Defaults to 0.
            y (int, optional): the y position of the text. Defaults to 0.
            font (str, optional): the text font. Defaults to 'Comic Sans MS'.
            fontSize (int, optional): the text size. Defaults to 50.
            color (tuple, optional): the text color. Defaults to (255, 255, 255).
        """
        self._font = pygame.font.SysFont(font, fontSize)
        self._color = color

        self._window = window

        self._x = x
        self._y = y
        self._text = text
        self.textSurface = self._font.render(self._text, True, self._color)

    @property
    def text(self, newText):
        """replaces the text stored in the class with newText and rerenders the text with the new message

        Args:
            newText (_type_): if the new text is not a string convert it to a string
        """
        if type(newText) != str:
            newText = str(newText)
        
        self._text = newText
        self.textSurface = self._font.render(self._text, True, self._color)

    @property
    def color(self):
        """shows the color of the text

        Returns:
            _type_: text color
        """
        return self._color
    
    @property
    def x(self):
        """shows the x position of the text

        Returns:
            int: text position (x)
        """
        return self._x
    
    @property
    def y(self):
        """shows the x position of the text

        Returns:
            int: text position (x)
        """
        return self._y
    
    @property
    def pos(self):
        """shows the postion of the text (x,y)

        Returns:
            _type_: text postion (x,y)
        """
        return (self.x, self.y)
    
    @color.setter
    def color(self, col):
        """sets a new color for the player

        Args:
            col (_type_): col represents the new color
        """        

        self._color = col

    @x.setter
    def x(self, new_x):
        """sets a new x position for the text

        Args:
            new_x (int): new text position (x)
        """
        self._x = new_x
    
    @y.setter
    def y(self, new_y):
        """sets a new y position for the text

        Args:
            new_y (int): new text position (y)
        """
        self._y = new_y

    def draw(self):
        """draws the text on the string using the (x,y) position
        """
        self._window.blit(self.textSurface, self.pos)
