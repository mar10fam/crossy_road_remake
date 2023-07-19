import pygame
class Bus(pygame.sprite.Sprite):
    LEFT_IMAGE = pygame.image.load('resources/bus_left.png')
    RIGHT_IMAGE = pygame.image.load('resources/bus_right.png')

    STARTING_POSITION = (300, 250)
    SIZE = (60, 30)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 2

    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = Bus.LEFT_IMAGE if direction == 'Left' else Bus.RIGHT_IMAGE
        self.rect = pygame.Rect((0, 0), Bus.SIZE)
        self.rect.center = Bus.STARTING_POSITION
        self.direction = direction
    def move(self):
        # bus is going left
        if self.direction == 'Left':
            self.rect.centerx -= Bus.MOVE_DIST
            # bus has moved off the screen
            if self.rect.right <= 0:
                self.rect.centerx = Bus.SCREEN_DIM[0] + (Bus.SIZE[0] / 2)
        # bus is going right
        else:
            self.rect.centerx += Bus.MOVE_DIST
            # bus has moved off the screen
            if self.rect.left >= Bus.SCREEN_DIM[0]:
                self.rect.centerx = -Bus.SCREEN_DIM[0] / 2








