import pygame
from frog import Frog

pygame.init()

SCREEN_DIM = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)

pygame.display.set_caption('Frog Road!')

CLOCK = pygame.time.Clock()
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (28, 128, 28)
YELLOW = (100, 85, 0)
BROWN = (118, 92, 72)
GRAY = (175, 175, 175)
BLUE = (0, 0, 175)

frog = Frog()

while True:

    CLOCK.tick(FPS)
    SCREEN.fill(BLACK)

    SCREEN.blit(frog.image, frog.rect)

    pygame.display.flip()

    event = pygame.event.wait()
    if event.type == pygame.QUIT: 
        break

pygame.quit()