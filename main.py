# IMPORT----------------------------------------------------------------------------------------------------------------


import pygame
pygame.init()


# CONSTANTS-------------------------------------------------------------------------------------------------------------


WIDTH = 1900
HEIGHT = 1000
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

FPS = 60

x = HALF_WIDTH
y = HALF_HEIGHT
player_speed = 2
is_jump = False
jump_count = 10
fly = False
TILE = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# COLORS----------------------------------------------------------------------------------------------------------------


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)


# MAP-------------------------------------------------------------------------------------------------------------------


text_map = [
    'WWWWWWWWWWWWWWWWWWW',
    'W......W..........W',
    'W..WWW...W........W',
    'W....W..WW........W',
    'W..W....W.........W',
    'W..W...WWW........W',
    'W....W............W',
    'W....W............W',
    'W....W............W',
    'WWWWWWWWWWWWWWWWWWW'
]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))


# GAME------------------------------------------------------------------------------------------------------------------


while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if keys[pygame.K_e] and fly is False:
        fly = True
        y -= 5

    elif keys[pygame.K_q] and fly is True:
        fly = False
        y += 5

    if keys[pygame.K_w]:
        if fly is True:
            y -= player_speed + 3
        else:
            y -= player_speed
    if keys[pygame.K_s]:
        if fly is True:
            y += player_speed + 3
        else:
            y += player_speed
    if keys[pygame.K_a]:
        if fly is True:
            x -= player_speed + 3
        else:
            x -= player_speed
    if keys[pygame.K_d]:
        if fly is True:
            x += player_speed + 3
        else:
            x += player_speed

    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (x, y, 30, 30))
    for x_m, y_m in world_map:
        pygame.draw.rect(screen, DARKGRAY, (x_m, y_m, TILE, TILE), 3)

    pygame.display.flip()
    clock.tick(FPS)
