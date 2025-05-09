import pygame
from pygame import *
from Arrow import arrow
import math

class knight():
    scale_factor = 1

    def __init__(self, window, imageFile1 = 'Images/Knight1.png', imageFile2 = 'Images/Knight1.png',
                 imageFile3 = 'Images/Knight1.png', x_speed = 4, 
                 movement_keys = {'left': K_LEFT, 'right': K_RIGHT}):
        """__init__ initializes the player character, the size of the image, the size of the hitbox,
        and variables referenced later within the class.

        Args:
            window (_type_): the pygame display
            imageFile1 (str, optional): first player image. Defaults to 'Images/Knight1.png'.
            imageFile2 (str, optional): second player image. Defaults to 'Images/Knight1.png'.
            imageFile3 (str, optional): third player image. Defaults to 'Images/Knight1.png'.
            x_speed (int, optional): player movement speed. Defaults to 4.
            movement_keys (dict, optional): Horizontal key inputs. Defaults to {'left': K_LEFT, 'right': K_RIGHT}.
        """
        # Initialize Image and Rectangle
        self.imageFile1 = imageFile1
        self.image = pygame.image.load(self.imageFile1)
        self.image = pygame.transform.scale_by(self.image, self.scale_factor)
        self._rect = self.image.get_rect()

        # Pick starting position
        self._rect.x = (window.get_width()-self._rect.width)/2
        self._rect.y = 320

        # Set hitbox
        self._rect.width = 50
        self._rect.height = 50
        
        # Initialize Other Variables:
        self.__window = window
        self.x_speed = x_speed
        self.__movement_keys = movement_keys
        self.imageFile3 = imageFile3
        self.imageFile2 = imageFile2

                
    @property
    def rect(self):
        """shows the rect property

        Returns:
            _type_: rectangle dimensions
        """
        return self._rect
    
    @property
    def pos(self):
        """shows the player position

        Returns:
            int: player position (x,y)
        """
        return (self._rect.x, self._rect.y)
    
    @property
    def x(self):
        """shows the x position of the player

        Returns:
            int: player position (x)
        """        
        return self._rect.x
    
    @property
    def y(self):
        """shows the y position of the player

        Returns:
            int: player position (y)
        """
        return self._rect.y
    
    @x.setter
    def x(self, new_x):
        """sets a new x position for the player

        Args:
            new_x (int): new player position (x)
        """
        if 0 <= new_x < self.window.get_width():
            self._rect.x = new_x
    
    @y.setter
    def y(self, new_y):
        """sets a new y position for the player

        Args:
            new_y (int): new player position (y)
        """
        if 0 <= new_y < self.window.get_height():
            self._rect.y = new_y
    
    @property
    def x_speed(self):
        """shows the horizontal movement speed of the player

        Returns:
            int: horizontal player movement speed(_x_speed)
        """
        return self._x_speed
    
    @x_speed.setter
    def x_speed(self, new_speed):
        """sets a new movement speed for the player

        Args:
            new_speed (int): new player horizontal movement speed(new_speed)
        """
        self._x_speed = new_speed
        
    @property
    def movement_keys(self):
        """shows the movement keys for player movement as a dictionary with name:key_input

        Returns:
            dict: {'name':keyinput}
        """
        return self.__movement_keys
    
    @property
    def window(self):
        """shows the pygame display which the knight will be used in

        Returns:
            _type_: pygame display
        """
        return self.__window
    
    def manual_move(self):
        """Starts scanning key inputs, if left, and greater than a boundary, the player position is subtracted by the speed
        if right, and less than another boundary, the speed is added to the player position

        Returns:
            _type_: player position (x,y)
        """
        keysPressed = pygame.key.get_pressed()
    
        if keysPressed[self.movement_keys['left']]:
            if self.x >= 132:
                self.x -= abs(self.x_speed)
        if keysPressed[self.movement_keys['right']]:
            if self.x <= 395:
                self.x += abs(self.x_speed)
        return self.pos

    def collide(self, value):
        """checks for collisions between the knight and the arrow class if True returns True, if False, returns False

        Args:
            value (_type_): the arrow the knight may collide with

        Returns:
            boolean: True or False depending on arg
        """
        if isinstance(value, arrow):
            return self.rect.colliderect(value.rect)
        else:
            return False

    def draw(self, dt):
        """Takes in a time integer, and alternates between the three different imageFiles 1, 2, and 3 depending on the integer

        Args:
            dt (int): _description_
        """
        if math.floor(dt) % 3 == 2:
            self.image = pygame.image.load(self.imageFile3)
            self.image = pygame.transform.scale_by(self.image, self.scale_factor)
            self.window.blit(self.image, self.pos)
        elif math.floor(dt) % 3  == 1:
            self.image = pygame.image.load(self.imageFile2)
            self.image = pygame.transform.scale_by(self.image, self.scale_factor)
            self.window.blit(self.image, self.pos)
        elif math.floor(dt) % 3 == 0:
            self.image = pygame.image.load(self.imageFile1)
            self.image = pygame.transform.scale_by(self.image, self.scale_factor)
            self.window.blit(self.image, self.pos)
