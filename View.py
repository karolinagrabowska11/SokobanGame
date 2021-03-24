from cons import *
from images import wall_image, blue_store_image, blue_tiles_image

WALL_POSITIONS = []
BLUE_STORE_POSITIONS = []
BLUE_TILES_POSITIONS = []


class View:
    """Display game board, headline, scores and winning text.
    Saves positions of objects in lists: WALL_POSITIONS, BLUE_STORE_POSITIONS, BLUE_TILES_POSITIONS"""

    (width, height) = (570, 420)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Sokoban')
    screen.fill(LIGHT_BLUE)
    pygame.display.flip()

    map_level = map_level_1.splitlines()
    for row, line in enumerate(map_level):
        for column, value in enumerate(line):
            if value == 'w':
                WALL_POSITIONS.append((column * PICTURE_EDGE, row * PICTURE_EDGE))
            elif value == 's':
                BLUE_STORE_POSITIONS.append((column * PICTURE_EDGE, row * PICTURE_EDGE))
            else:
                BLUE_TILES_POSITIONS.append((column * PICTURE_EDGE, row * PICTURE_EDGE))

    def view_board(self, screen=screen):
        """Display board based on defined map."""

        for position in WALL_POSITIONS:
            screen.blit(wall_image, position)
        for position in STORE_POSITIONS:
            screen.blit(blue_store_image, position)
        for position in BLUE_TILES_POSITIONS:
            screen.blit(blue_tiles_image, position)

    def headline(self, screen, level):
        """Display welcome and level number on a screen."""

        my_font = pygame.font.SysFont('orange juice', 38)
        head_text = my_font.render('Welcome! You are playing Sokoban, Level %s' % level, True, WHITE)
        screen.blit(head_text, (2, 3))

    def winning(self, screen, points, max_points):
        """Display text when the players wins."""

        my_font = pygame.font.SysFont('orange juice', 100)
        if points == max_points:
            winning_text = my_font.render('!!! YOU WON !!!', True, LIGHT_GREEN)
            screen.blit(winning_text, (25, 160))

    def score(self, screen, points):
        """Display score on a screen."""

        my_font = pygame.font.SysFont('Comic Sans MS', 25)
        score_text = my_font.render('Score: %s' % points, True, BLACK)
        screen.blit(score_text, (430, 360))
