import copy
from cons import *
from images import crate_image, crate_store_image
from GameObject import GameObject


class Boxes(GameObject):
    """The class responsible for the box objects, their rotations and display"""

    def __init__(self):
        super().__init__()
        self.positions = copy.deepcopy(BOX_POSITIONS)
        self.image = crate_image

    def view_box(self, screen):
        """Display boxes"""

        image = crate_image
        for position in self.positions:
            if position in STORE_POSITIONS:
                image = crate_store_image
            screen.blit(image, position)
            image = crate_image

    def change_box_position(self, old_position, new_position):  # class box
        """Function get old and new box position and change old position to a new one in a boxes_positions list."""

        self.positions.remove(old_position)
        self.positions.append(new_position)
