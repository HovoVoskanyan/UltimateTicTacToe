import pygame
from Resources import Game
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

    for i in range(1, 9):
        pygame.draw.line(screen, BLACK, (CELL_SIZE * i, 0), (CELL_SIZE * i, HEIGHT), 2)  # Smaller vertical lines
        pygame.draw.line(screen, BLACK, (0, CELL_SIZE * i), (WIDTH, CELL_SIZE * i), 2)  # Smaller horizontal lines


# Function to draw X or O in a cell
def draw_symbol(row, col, symbol):
    x = col * CELL_SIZE
    y = row * CELL_SIZE

    if symbol == 'X':
        pygame.draw.line(screen, RED, (x + CELL_SIZE * 0.1, y + CELL_SIZE * 0.1), (x + CELL_SIZE * 0.8, y + CELL_SIZE * 0.8), LINE_WIDTH)
        pygame.draw.line(screen, RED, (x + CELL_SIZE * 0.1, y + CELL_SIZE * 0.8), (x + CELL_SIZE * 0.8, y + CELL_SIZE * 0.1), LINE_WIDTH)
    elif symbol == 'O':
        pygame.draw.circle(screen, BLUE, (int(x + CELL_SIZE / 2), int(y + CELL_SIZE / 2)), int(CELL_SIZE * 0.4), LINE_WIDTH)


# Function to draw the ultimate board
def draw_ultimate_board(ultimate_board):
    draw_grid()
    for i in range(9):
        for j in range(9):
            symbol = ''
            if ultimate_board[i][j] == 1:
                symbol = 'X'
            elif ultimate_board[i][j] == 2:
                symbol = 'O'
            draw_symbol(i, j, symbol)

    # Draw borders for the entire ultimate board

# Main game loop
def main():

    running = True
    game = Game.Game()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        # Example ultimate board
        if(game.is_game_over()):
            winner = game.big_board.check_winner()
            if(winner != 0):
                print(winner,"Has Won!")
                break

        # Draw the ultimate board
        draw_ultimate_board(game.big_board.visualize())

        best_move, time_taken = Game.monte_carlo(game, player=1, iterations=100)

        game.make_move(move = best_move,player=game.current_player)

        randomMove = game.random_move()

        if(randomMove is not None):
            game.make_move(move = randomMove,player=game.current_player)

        # Print the result
        print("Best Move:", best_move)
        print("Time Taken:", time_taken, "seconds")
        # Update the display
        pygame.display.flip()

        # Control the frame rate
        pygame.time.Clock().tick(FPS)

        screen.fill(WHITE)


if __name__ == "__main__":
    main()
