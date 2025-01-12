import pygame
from pygame.locals import *
from constants import *
from entity import Entity

class Ghost(Entity):
    def __init__(self, node):
        Entity.__init__(self, node)
        self.name = GHOST
        self.points = 200