import pygame
import os

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

def check():
    pass

def get_player_info(player, relative_pos):
    p = pygame.transform.scale(pygame.image.load(f"{player}.png"), (60, 60))
    pos = get_abs_pos(relative_pos)
    return p, pos

def get_abs_pos(pos):
    
    # const variable for row range
    X_FIRST_BLOCK = 40 <= pos["x"] < 115
    X_SECOND_BLOCK = 115 <= pos["x"] < 185
    X_THIRD_BLOCK = 190 <= pos["x"] < 255

    # const variable for column range
    Y_BLOCK_0 = 80 < pos["y"] <= 150
    Y_BLOCK_1 = 150 < pos["y"] <= 200
    Y_BLOCK_2 = 200 < pos["y"] <= 300
    
    # ================================================================

    # block 0 0
    if  X_FIRST_BLOCK and Y_BLOCK_0:
        return (45, 85)

    # block 0 1
    elif X_SECOND_BLOCK and Y_BLOCK_0:
        return (120, 85)
    
    # block 0 2
    elif X_THIRD_BLOCK and Y_BLOCK_0:
        return (190, 85)
    
    # end block 0

    # ================================================================

    # block 1 0
    if X_FIRST_BLOCK and Y_BLOCK_1:
        return (45, 155)
    
    # block 1 1
    elif X_SECOND_BLOCK and Y_BLOCK_1:
        return (120, 155)
    
    # block 1 2
    elif X_THIRD_BLOCK and Y_BLOCK_1:
        return (190, 155)
    
    # end block 1

    # ================================================================

    # block 2 0
    if X_FIRST_BLOCK and Y_BLOCK_2:
        return (45, 230)
    
    # block 2 1
    elif X_SECOND_BLOCK and Y_BLOCK_2:
        return (120, 230)
    
    # block 2 2
    elif X_THIRD_BLOCK and Y_BLOCK_2:
        return (190, 230)
    
    # end block 2

    # ================================================================

pygame.init()
x, y = 300, 300
screen = pygame.display.set_mode((x, y))
clock = pygame.time.Clock()
running = True


box = pygame.image.load('board.png')

screen.fill("black")
screen.blit(box, (x // 8, y // 4))
player = "O"

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = dict(x=event.dict["pos"][0], y=event.dict["pos"][1])

            image, pos = get_player_info(player, mouse_pos)
            
            screen.blit(image, (pos))

            player = "O" if player == "X" else "X"
    
        
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()