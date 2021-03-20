import pygame
import sys
import copy
from cons import *
from images import *

WALL_POSITIONS = []
BLUE_STORE_POSITIONS = []
BLUE_TILES_POSITIONS = []


class GameObject:
    def __init__(self):
        self.position = (0, 0)
        self.image = 0

    def view_object(self):
        pass


class Boxes(GameObject):
    def __init__(self):
        super().__init__()
        self.positions = copy.deepcopy(BOX_POSITIONS)
        self.image = crate

    def view_box(self, screen):
        """Display boxes"""

        image = crate
        for position in self.positions:
            if position in STORE_POSITIONS:
                image = crate_store
            screen.blit(image, position)
            image = crate

    def change_box_position(self, old_position, new_position):  # class box
        """Function get old and new box position and change old position to a new one in a boxes_positions list."""

        self.positions.remove(old_position)
        self.positions.append(new_position)


class Player(GameObject):
    img_player = {'UP': player_img_up, 'DOWN': player_img_down, 'RIGHT': player_img_right, 'LEFT': player_img_left,
                  'STORE_UP': player_img_store_up, 'STORE_DOWN': player_img_store_down,
                  'STORE_RIGHT': player_img_store_right, 'STORE_LEFT': player_img_store_left}

    def __init__(self):
        super().__init__()
        self.position = (330, 300)
        self.image = player_img_up
        self.store_positions = STORE_POSITIONS
        self.score = 0

    def get_score(self, boxes):
        """Return score number"""

        return len(set(boxes.positions).intersection(self.store_positions))

    def view_player(self, screen):
        """Display player"""

        screen.blit(self.image, self.position)

    def turn(self, direction_key, box):
        """Handle player's turnover.
         If player wants to go towards the wall, nothing is nothing changes.
         If player wants to go towards the box with the wall or another box behind, only the picture changes.
         Else player image and position changes."""

        image = self.img_player[direction_key]
        direction = DIRECTIONS[direction_key]

        position_x, position_y = self.position
        direction_x, direction_y = direction
        new_position = (position_x + direction_x, position_y + direction_y)
        new_box_position = (position_x + 2 * direction_x, position_y + 2 * direction_y)
        if new_position in WALL_POSITIONS:
            return
        if new_position in box.positions and (new_box_position in WALL_POSITIONS or new_box_position in box.positions):
            self.image = image
            if new_position in STORE_POSITIONS:
                self.image = self.img_player[STORE_PREFIX + direction_key]
            return
        if new_position in box.positions:
            self.position = new_position
            self.image = image
            box.change_box_position(new_position, new_box_position)
            if new_position in STORE_POSITIONS:
                self.image = self.img_player[STORE_PREFIX + direction_key]
            return
        self.position = new_position
        self.image = image
        if new_position in STORE_POSITIONS:
            self.image = self.img_player[STORE_PREFIX + direction_key]


class View:
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
            screen.blit(blue_store, position)
        for position in BLUE_TILES_POSITIONS:
            screen.blit(blue_tiles, position)


def score(screen, points):
    """Display score on a screen."""

    my_font = pygame.font.SysFont('Comic Sans MS', 25)
    score_text = my_font.render('Score: %s' % points, True, BLACK)
    screen.blit(score_text, (430, 360))


def headline(screen, level):
    """Display welcome and level number on a screen."""

    my_font = pygame.font.SysFont('orange juice', 38)
    head_text = my_font.render('Welcome! You are playing Sokoban, Level %s' % level, True, WHITE)
    screen.blit(head_text, (2, 3))


def winning(screen, points, max_points):
    """Display text when the players wins."""

    my_font = pygame.font.SysFont('orange juice', 100)
    if points == max_points:
        winning_text = my_font.render('!!! YOU WON !!!', True, LIGHT_GREEN)
        screen.blit(winning_text, (25, 160))


def restart_game(screen):
    """Display information what to do to restart the game."""

    my_font = pygame.font.SysFont('orange juice', 30)
    restart_text = my_font.render('Press R to restart the game.', True, WHITE)
    screen.blit(restart_text, (150, 395))


def game_loop(clock, view, player, boxes, screen):
    """Starts the game and handle keyboard."""

    running = True
    while running:
        clock.tick(10)
        view.view_board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.turn('RIGHT', boxes)
                elif event.key == pygame.K_LEFT:
                    player.turn('LEFT', boxes)
                elif event.key == pygame.K_UP:
                    player.turn('UP', boxes)
                elif event.key == pygame.K_DOWN:
                    player.turn('DOWN', boxes)
                elif event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                elif event.key == pygame.K_r:
                    player.__init__()
                    boxes.__init__()
        boxes.view_box(screen)
        player.view_player(screen)
        screen.blit(screen, (0, 0))
        score(screen, player.get_score(boxes))
        headline(screen, level=1)
        winning(screen, player.get_score(boxes), 6)
        restart_game(screen)
        pygame.display.update()


def main():
    init_status = pygame.init()
    if init_status[1] > 0:
        print('%s errors... Exiting...' % init_status[1])
        sys.exit()
    else:
        print('Welcome in PyGame - Sokoban!')

    clock = pygame.time.Clock()
    view = View()
    screen = view.screen
    player = Player()
    boxes = Boxes()

    game_loop(clock=clock, view=view, player=player, boxes=boxes, screen=screen)


main()
