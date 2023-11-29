# Function to display the Tic Tac Toe board

import pygame
import sys

# Initialize Pygame
pygame.init()
# Constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = WIDTH // 9
LINE_WIDTH = 15
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultimate Tic-Tac-Toe")

# Function to draw the game grid
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (CELL_SIZE * i * 3, 0), (CELL_SIZE * i * 3, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (0, CELL_SIZE * i * 3), (WIDTH, CELL_SIZE * i * 3), LINE_WIDTH)

# Function to draw X or O in a cell
def draw_symbol(row, col, symbol):
    x = col * CELL_SIZE * 3 + CELL_SIZE * 1.5
    y = row * CELL_SIZE * 3 + CELL_SIZE * 1.5

    if symbol == 'X':
        pygame.draw.line(screen, RED, (x - CELL_SIZE, y - CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, RED, (x - CELL_SIZE, y + CELL_SIZE), (x + CELL_SIZE, y - CELL_SIZE), LINE_WIDTH)
    elif symbol == 'O':
        pygame.draw.circle(screen, BLUE, (int(x), int(y)), CELL_SIZE, LINE_WIDTH)

# Function to draw the ultimate board
# Function to draw the ultimate board
def draw_ultimate_board(ultimate_board):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    symbol = ''
                    if ultimate_board[i * 3 + k][j * 3 + l] == 1:
                        symbol = 'X'
                    elif ultimate_board[i * 3 + k][j * 3 + l] == 2:
                        symbol = 'O'
                    draw_symbol(i * 3 + k + j * 9, j * 3 + l + i * 9, symbol)

            # Draw borders for each small board
            pygame.draw.rect(screen, BLACK,
                             (i * CELL_SIZE * 3 + j * CELL_SIZE * 9, j * CELL_SIZE * 3 + i * CELL_SIZE * 3 , CELL_SIZE * 9, CELL_SIZE * 3),
                             LINE_WIDTH)

    # Draw borders for the entire ultimate board
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HEIGHT), LINE_WIDTH)

# Main game loop



def display_board(small_board,ultimate_board ):
    print(f"Printing Ultimate board")

    for i in range(len(ultimate_board)):
        if i % 3 == 0 and i > 0:
            print("-" * 21)
        for j in range(len(ultimate_board[i])):
            if j % 3 == 0 and j > 0:
                print("|", end=" ")  # Separator for every three columns

            if ultimate_board[i][j] == 0:
                print("*", end=" ")
            elif ultimate_board[i][j] == 1:
                print("X", end=" ")
            elif ultimate_board[i][j] == 2:
                print("O", end=" ")
        print()

    print(f"\nPrinting small board \n")

    for i in range(len(small_board)):
        print("-" * 10,end="\n")  # Separator line for every three rows
        for j in range(len(small_board[i])):
            print("|", end="")  # Separator for every three columns

            if small_board[i][j] == 0:
                print("*", end=" ")

            elif small_board[i][j] == 1:
                print("X", end=" ")

            elif small_board[i][j] == 2:
                print("O", end=" ")
            if(j==len(small_board[i])-1):
                print("|", end="")  # Separator for every three columns
        print()
        if (i == len(small_board) - 1):
            print("-" * 10, end="\n")  # Separator line for every three rows
def main():


    small_board_example = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        # Example ultimate board
        ultimate_board_example = [
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        # Draw the ultimate board
        draw_ultimate_board(ultimate_board_example)

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        pygame.time.Clock().tick(FPS)


if __name__ == "__main__":
    main()
