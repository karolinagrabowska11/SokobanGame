import pygame

PICTURE_EDGE = 30

UP = (0, -PICTURE_EDGE)
DOWN = (0, PICTURE_EDGE)
RIGHT = (PICTURE_EDGE, 0)
LEFT = (-PICTURE_EDGE, 0)

DIRECTIONS = {'UP': (0, -PICTURE_EDGE), 'DOWN': (0, PICTURE_EDGE),
              'RIGHT': (PICTURE_EDGE, 0), 'LEFT': (-PICTURE_EDGE, 0)}

STORE_PREFIX = 'STORE_'

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
BLUE = pygame.Color(0, 0, 255)
LIGHT_BLUE = pygame.Color(179, 204, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
LIGHT_GREEN = pygame.Color(128, 255, 212)
YELLOW = pygame.Color(255, 255, 0)

map_level_1 = """
wwwwwwwwwwwwwwwwwww
w   wwwww         w
w   w   w         w
w   wc cw         w
w www   ww        w
w w   c  w        w
www wcww w   wwwwww
w   w ww wwwww  ssw
w c c           ssw
wwwww www w ww  ssw
w   w     wwwwwwwww
wwwwwwwwwwwwwwwwwww"""

BOX_POSITIONS = [(120, 270), (60, 270), (150, 210), (180, 180), (150, 120), (210, 120)]
STORE_POSITIONS = [(480, 300), (510, 300), (480, 270), (510, 270), (480, 240), (510, 240)]