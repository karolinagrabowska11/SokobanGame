from images import *
from Player import Player
from Boxes import Boxes
from View import View
from Game import Game


def main():
    clock = pygame.time.Clock()
    view = View()
    screen = view.screen
    player = Player()
    boxes = Boxes()
    game = Game()
    game.game_loop(clock=clock, view=view, player=player, boxes=boxes, screen=screen)


main()
