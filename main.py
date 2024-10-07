import pygame

def check(board, player_name):
    
    for row in range(3):
        buff = ""
        for col in range(3):
            
            if board[row][col] == player_name:
                buff += player_name
            
            if len(buff) == 3:
                return True

    for col in range(3):
        buff = ""
        for row in range(3):

            if board[row][col] == player_name:
                buff += player_name

            if len(buff) == 3:
                return True

    buff = ""
    for row_col in range(3):
        
        if board[row_col][row_col] == player_name:
            buff += player_name

        if len(buff) == 3:
            return True

    buff = ""
    for row, col in enumerate(range(2, 0, -1)):
        
        if board[row][col] == player_name:
            buff += player_name
        
        if len(buff) == 3:
            return True

    return False

def put_in_board(board, player_name, row, col):
    board[row][col] = player_name

def get_player_info(player_name, relative_pos):
    p = pygame.transform.scale(pygame.image.load(f"./asset/{player_name}.png"), (60, 60))
    pos, row, column = get_abs_pos(relative_pos)
    return p, pos, row, column

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
        return (45, 85), 0, 0

    # block 0 1
    elif X_SECOND_BLOCK and Y_BLOCK_0:
        return (120, 85), 0, 1
    
    # block 0 2
    elif X_THIRD_BLOCK and Y_BLOCK_0:
        return (190, 85), 0, 2
    
    # end block 0

    # ================================================================

    # block 1 0
    if X_FIRST_BLOCK and Y_BLOCK_1:
        return (45, 155), 1, 0
    
    # block 1 1
    elif X_SECOND_BLOCK and Y_BLOCK_1:
        return (120, 155), 1, 1
    
    # block 1 2
    elif X_THIRD_BLOCK and Y_BLOCK_1:
        return (190, 155), 1, 2
    
    # end block 1

    # ================================================================

    # block 2 0
    if X_FIRST_BLOCK and Y_BLOCK_2:
        return (45, 230), 2, 0
    
    # block 2 1
    elif X_SECOND_BLOCK and Y_BLOCK_2:
        return (120, 230), 2, 1
    
    # block 2 2
    elif X_THIRD_BLOCK and Y_BLOCK_2:
        return (190, 230), 2, 2
    
    # end block 2

    # ================================================================

def main():

    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
    
    pygame.init()
    x, y = 300, 300
    screen = pygame.display.set_mode((x, y))
    clock = pygame.time.Clock()
    running = True

    box = pygame.image.load('./asset/board.png')

    screen.fill("black")
    screen.blit(box, (x // 8, y // 4))
    player = "O"

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                # get mouse position in screen
                mouse_pos = dict(x=event.dict["pos"][0], y=event.dict["pos"][1])

                # get player information
                image, icon_pos, row, column = get_player_info(player, mouse_pos)
                
                # Checks that the item selected by the player has not been used before
                if board[row][column] != "":
                    continue
                
                # put image in screen and its name(X|O) in board
                put_in_board(board, player, row, column)
                screen.blit(image, (icon_pos))

                # check state to win
                if check(board, player):
                    main()
                    print(f"{player}")

                # switch player
                player = "O" if player == "X" else "X"
        
        pygame.display.flip()

        clock.tick(120)

    pygame.quit()

if __name__ == "__main__":
    main()