import pygame
from pygame.locals import *
from vector import Vector
from constants import *
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # Logs to console
    ]
)

class Pacman(object):

    def __init__(self, node):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug("Initializing Pacman")
        self.name = PACMAN
        # self.position = Vector(200, 400)
        self.directions = {
            STOP: Vector(),
            UP: Vector(0,-1),
            DOWN: Vector(0,1),
            LEFT: Vector(-1,0),
            RIGHT: Vector(1,0)
        }
        self.direction = STOP
        self.speed = 100 * TILEWIDTH/16
        self.radius = 10
        self.color = YELLOW
        self.node = node
        self.setPosition()
        self.target = node
        self.collideRadius = 5

    def eatPellets(self, pelletList):
        for pellet in pelletList:
            d = self.position - pellet.position
            dSquared = d.magnitudeSquared()
            rSquared = (pellet.radius + self.collideRadius)**2
            if dSquared <= rSquared:
                return pellet
        return None

    def setPosition(self):
        self.logger.debug(f"Setting position to {self.node.position}")
        self.position = self.node.position.copy()

    def update(self, dt):
        self.logger.debug(f"Updating position with dt={dt}")
        self.position += self.directions[self.direction]*self.speed*dt
        direction = self.getValidKey()
        # self.direction = direction
        # self.node = self.getNewTarget(direction)
        # self.setPosition()
        if self.overshotTarget():
            self.logger.debug("Overshot target, updating node and target")
            self.node = self.target
            if self.node.neighbors[PORTAL] is not None:
                self.node = self.node.neighbors[PORTAL]
            self.target = self.getNewTarget(direction)
            if self.target is not self.node:
                self.direction = direction
            else:
                self.target = self.getNewTarget(self.direction)
            if self.target is self.node:
                self.direction = STOP
            self.setPosition()
        else:
            if self.oppositeDirection(direction):
                self.reverseDirection()

    def validDirection(self, direction):
        if direction is not STOP:
            if self.node.neighbors[direction] is not None:
                return True
        return False
    
    def reverseDirection(self):
        self.direction *= -1
        temp = self.node
        self.node = self.target
        self.target = temp

    def oppositeDirection(self, direction):
        if direction is not STOP:
            if direction == self.direction * -1:
                return True
        return False
    
    def getNewTarget(self, direction):
        if self.validDirection(direction):
            return self.node.neighbors[direction]
        return self.node

    def getValidKey(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP]:
            return UP
        if key_pressed[K_DOWN]:
            return DOWN
        if key_pressed[K_LEFT]:
            return LEFT
        if key_pressed[K_RIGHT]:
            return RIGHT
        return STOP
    
    def overshotTarget(self):
        if self.target is not None:
            vec1 = self.target.position - self.node.position
            vec2 = self.position - self.node.position
            node2Target = vec1.magnitudeSquared()
            node2Self = vec2.magnitudeSquared()
            return node2Self >= node2Target
        return False
    
    def render(self, screen):
        p = self.position.asTuple()
        pygame.draw.circle(screen, self.color, p, self.radius)