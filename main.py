import pygame 

import random

pygame.init()

# class Dog:

#     def __init__(self):
#         self.age=7
#         self.name="ralph"
#     def jump(self):
#         print ("jumpingupanddown")

# dog = Dog()
# dog.jump()
BLOCKSIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = 1010
SCREEN_HEIGHT = 800

BLACK = (0,0,0)
WHITE = (255,255,255)

COLORS = [
    (235, 171, 52), #yellow
    (255,0,0), #red
    (0,255,0), #green
    (0,0,255), #blue
    (235, 131, 52), #orange
    (52, 217, 235), #cyan
    (128, 52, 235)  #purple
]
SHAPES = [
    [[1,1], [1,1]], #BLOCKSHAPE
    [[1,1,0], [0,1,1]], #Z SHAPE
    
          
          ]
