class GameObject:
    """Super class of the game objects: Player and Box objects"""

    def __init__(self):
        self.position = (0, 0)
        self.image = 0

    def view_object(self, screen):
        """Display object"""
        screen.blit(self.image, self.position)
