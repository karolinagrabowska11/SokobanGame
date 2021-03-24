import sys
from images import *
from cons import WHITE


class Game:
    """The class responsible for main game loop, handling keyboard and restarting whole game"""

    def restart_game(self, screen):
        """Display information what to do to restart the game."""

        my_font = pygame.font.SysFont('orange juice', 30)
        restart_text = my_font.render('Press R to restart the game.', True, WHITE)
        screen.blit(restart_text, (150, 395))

    def game_loop(self, clock, view, player, boxes, screen):
        """Starts the game and handle keyboard."""

        init_status = pygame.init()
        if init_status[1] > 0:
            print('%s errors... Exiting...' % init_status[1])
            sys.exit()
        else:
            print('Welcome in PyGame - Sokoban!')

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
            view.score(screen, player.get_score(boxes))
            view.headline(screen, level=1)
            view.winning(screen, player.get_score(boxes), 6)
            self.restart_game(screen)
            pygame.display.update()
