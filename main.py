import pygame, sys, random
from frog import Frog
from bus import Bus
from street import Street
from river import River
from log import Log

pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])

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
log = Log(Log.STARTING_POSITION, 'Right')

# Street
streets = []
number_of_buses = 3
street_height = 400
for _ in range(2):
    streets.append(Street(street_height, 'Left', random.randint(1, number_of_buses)))
    streets.append(Street(street_height - 40, 'Right', random.randint(1, number_of_buses)))
    street_height -= 80

# River
rivers = []
number_of_logs = 3
river_height = 200
for _ in range(2):
    rivers.append(River(river_height, 'Left', random.randint(1, number_of_logs)))
    rivers.append(River(river_height - 30, 'Right', random.randint(1, number_of_logs)))
    river_height -= 60

# Scoring
score = 0
current_best = 0
high_score = 0

while True:

    CLOCK.tick(FPS)
    SCREEN.fill(GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # W
                frog.move_up()
            if event.key == pygame.K_a:  # A
                frog.move_left()
            if event.key == pygame.K_s:  # S
                frog.move_down()
            if event.key == pygame.K_d:  # D
                frog.move_right()

    for street in streets:
        SCREEN.fill(GRAY, street.rect)
        for bus in street.buses:
            SCREEN.blit(bus.image, bus.rect)
            bus.move()
            if frog.rect.colliderect(bus.rect):
                frog.reset_position()

    if frog.rect.colliderect(log.rect):
        frog.move_on_log(log)

    log.move()

    # Act on rivers and logs
    frog_on_log = False
    for river in rivers:
        # Draw River
        SCREEN.fill(BLUE, river.rect)

        # Log
        for log in river.logs:
            SCREEN.blit(log.image, log.rect)
            log.move()
            if frog.rect.colliderect(log.rect):
                frog.move_on_log(log)
                frog_on_log = True

        # Collided with River and not a Log
        if not frog_on_log and frog.rect.colliderect(river.rect):
            frog.reset_position()

    # Update score
    if 475 - frog.rect.top > current_best:
        current_best = 475 - frog.rect.top
    #update high score
    if score + current_best >= high_score:
        high_score = score + current_best
    # If player reaches end
    if frog.rect.top <= 60:
        frog.reset_position()
        frog.lives += 1
        score += 1000 + current_best
        current_best = 0
    # Print statements to view score
    print("Score: " + str(score + current_best))
    print("High Score: " + str(high_score))
    print("Lives: " + str(frog.lives))

    SCREEN.blit(frog.image, frog.rect)

    pygame.display.flip()


pygame.quit()