import pygame

# Initialize Pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Globals
player_x = 50


# Initialize Screen
size = (1000, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Sandbox")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
done = False
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- LOGIC
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player_x += 5

    # --- DRAWING
    screen.fill(WHITE)

    pygame.draw.rect(screen, GREEN, [player_x, 100, 30, 30])

    # --- Update screen with what we've drawn
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
# ----------- End Main Program Loop ---------------

# Close the window and quit.
pygame.quit()


"""
# Import External Librarys
import pygame
import json
import random


# Create walls,only run once
class Wall:
    def __init__(self, length, width, x, y):
        self.length = length
        self.width = width
        self.x = x
        self.y = y
        self.collision_x = x + length
        self.collision_y = y + width


# item = Wall(30, 300, 500, 50)
# print(type(item))

def createWalls():
    wall_storage = []

    for i in range(3):
        walls_x = random.randrange(400, 600)
        walls_y = random.randrange(0, 100)
        walls = vars(Wall(20, 300, walls_x, walls_y))
        wall_storage.append(walls)
        print("mark1")

    print(wall_storage)

    with open('walls.json', 'w') as walls_list:
        json.dump(wall_storage, walls_list)



# Load walls from Json file
with open("walls.json", "r") as wall_data_output:
    walls_list = json.load(wall_data_output)

print()




# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 540))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)



# drawing the walls
def drawWalls(walls_list):
    for walls in walls_list:
        pygame.draw.rect(screen, "grey", [walls['x'], walls['y'], walls['length'], walls['width']])
        pygame.display.flip()

def collisionDetect(player, wall):
    return wall['collision_x'] >= player.x >= wall['x']-30 and wall['y']-30 <= player.y <= wall['collision_y']


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    pygame.draw.rect(screen, "black", [player_pos.x, player_pos.y, 30, 30])

    drawWalls(walls_list)




    # collision detection

    # for wall in walls_list:
    #     print(collisionDetect(player_pos, wall))
    #     if wall['collision_x'] >= player_pos.x >= wall['x']-30 and player_pos.y >:
    #         player_pos.x = wall['x']-30
    #     elif wall['collision_x'] <= player_pos.x:
    #         player_pos.x = wall['collision_x']
    #     elif wall['y']-30 <= player_pos.y and wall['collision_x'] >= player_pos.x >= wall['x']-30:
    #         player_pos.y = wall['y'] - 30
    #     elif player_pos.y <= wall['collision_y']:
    #         player_pos.y = wall['collision_y']

    # print(player_pos.x, player_pos.y)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

"""

