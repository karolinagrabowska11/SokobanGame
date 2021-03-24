from cons import *
from images import *
from GameObject import GameObject
from View import WALL_POSITIONS


class Player(GameObject):
    """The class responsible for the player object, its movement, rotation, display and scored points"""

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
