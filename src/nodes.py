import pygame
from vector import Vector
from constants import *
import numpy as np
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # Logs to console
    ]
)

class Node:

    def __init__(self, x, y):
        self.position = Vector(x, y)
        self.neighbors = {
            UP: None,
            DOWN: None,
            LEFT: None,
            RIGHT: None,        
        }

    def render(self, screen):
        for n in self.neighbors.keys():
            if self.neighbors[n] is not None:
                line_start = self.position.asTuple()
                line_end = self.neighbors[n].position.asTuple()
                pygame.draw.line(screen, WHITE, line_start, line_end, 4)
                pygame.draw.circle(screen, RED, self.position.asIntTuple(), 12)


class NodeGroup(object):
    def __init__(self, level):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.nodeList = []
        self.level = level
        self.nodesLUT = {}
        self.nodeSymbols = ['+']
        self.pathSymbols = ['.']
        data = self.readMazeFile(level)
        self.logger.info(f"dataAfterReadFile: {data}")
        self.createNodeTable(data)
        self.connectHorizontally(data)
        self.connectVertically(data)

    def readMazeFile(self, textFile):
        return np.loadtxt(textFile, dtype='<U1')
    
    def createNodeTable(self, data, xoffset=0, yoffset=0):
        for row in list(range(data.shape[0])):
            for col in list(range(data.shape[1])):
                if data[row][col] in self.nodeSymbols:
                    x, y =self.constructKey(col+xoffset, row+yoffset)
                    self.nodesLUT[(x, y)] = Node(x, y)
                    self.logger.info(f"Added node: {(x ,y)}")
    
    def connectHorizontally(self, data, xoffset=0, yoffset=0):
        self.logger.info(f"[connectHorizontally] data: {data}")
        for node_key, node in self.nodesLUT.items():
            self.logger.info(f"Node:{node_key}, Connections: {node.neighbors}")
        for row in list(range(data.shape[0])):
            key = None
            for col in list(range(data.shape[1])):
                if data[row][col] in self.nodeSymbols:
                    if key is None:
                        key = self.constructKey(col+xoffset, row+yoffset)
                        self.logger.info(f"key: {key}")
                    else:
                        otherkey = self.constructKey(col+xoffset, row+yoffset)
                        self.nodesLUT[key].neighbors[RIGHT] = self.nodesLUT[otherkey]
                        self.nodesLUT[otherkey].neighbors[LEFT] = self.nodesLUT[key]
                        self.logger.info(f"Connecting horizontally: {key} <-> {otherkey}")
                        key = otherkey
                elif data[row][col] not in self.pathSymbols:
                    key = None

    def connectVertically(self, data, xoffset=0, yoffset=0):
        dataT = data.transpose()
        for col in list(range(dataT.shape[0])):
            key = None
            for row in list(range(dataT.shape[1])):
                if dataT[col][row] in self.nodeSymbols:
                    if key is None:
                        key = self.constructKey(col+xoffset, row+yoffset)
                    else:
                        otherkey = self.constructKey(col+xoffset, row+yoffset)
                        self.nodesLUT[key].neighbors[DOWN] = self.nodesLUT[otherkey]
                        self.nodesLUT[otherkey].neighbors[UP] = self.nodesLUT[key]
                        key = otherkey
                elif dataT[col][row] not in self.pathSymbols:
                    key = None

    def getNodeFromPixels(self, xpixel, ypixel):
        if (xpixel, ypixel) in self.nodesLUT.keys():
            return self.nodesLUT[(xpixel, ypixel)]
        return None

    def getNodeFromTiles(self, col, row):
        x, y = self.constructKey(col, row)
        if (x, y) in self.nodesLUT.keys():
            return self.nodesLUT[(x, y)]
        return None

    def constructKey(self, x, y):
        return x*TILEWIDTH, y*TILEHEIGHT
    
    def getStartTempNode(self):
        nodes = list(self.nodesLUT.values())
        return nodes[0]

    def render(self, screen):
        for node in self.nodesLUT.values():
            node.render(screen)