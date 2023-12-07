import time

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
    screen.fill(WHITE)
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


def main():

    is_settled = True
    userinput = 0
    while(is_settled):
        print("Please Select a Number\n 1- for Initializing MinMax algorithm agains Random Agent \n 2- for initializing Alpha Beta Pruning Algorithm Against Random Agent \n 3- for initializing Monte Carlo Algorithm against Random Agent")
        userinput = int(input("Enter Integer Number!\n"))
        if(userinput == 1 or userinput ==2 or userinput == 3):
            is_settled = False

    running = True

    last_move = None
    winners = list()
    move_times = list()
    for i in range(250):
        game = Game.Game()

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            visual = game.big_board.visualize()
            draw_ultimate_board(visual)

            if(game.is_game_over()):

                winner = game.big_board.check_winner()
                winners.append(winner)

                visual = game.big_board.visualize()
                draw_ultimate_board(visual)

                if(winner != 0 or winner != None):
                    if(winner ==1):
                        winner = "X"
                    elif(winner == 2):
                        winner = "O"
                    else:
                        winner = "Friendship"
                    print(winner,"Has Won!")
                    pygame.display.flip()

                    pygame.time.Clock().tick(FPS)
                    time.sleep(5)

                    screen.fill(WHITE)
                    break

            best_move,time_taken =None, None
            if(userinput == 1):
                best_move, time_taken = Game.minimax(game, depth=4, maximizing_player=1, last_move=last_move)

            elif(userinput ==2):
                best_move,time_taken = Game.alpha_beta(game,4,1,last_move)

            else:
                best_move, time_taken = Game.monte_carlo(game,player=1, iterations=1000, last_move=last_move)

            move_times.append(time_taken)
            game.make_move(move = best_move,player=game.current_player)


            last_move = best_move

            if (game.is_game_over()):

                visual = game.big_board.visualize()
                winner = game.big_board.check_winner()
                draw_ultimate_board(visual)
                winners.append(winner)

                if (winner != 0 or winner != None):
                    if (winner == 1):
                        winner = "X"
                    elif (winner == 2):
                        winner = "O"
                    else:
                        winner = "Friendship"
                    print(winner, "Has Won!")
                    pygame.display.flip()

                    pygame.time.Clock().tick(FPS)
                    time.sleep(5)

                    screen.fill(WHITE)
                    break


            randomMove = game.random_move(last_move=last_move)

            if(randomMove is not None):
                game.make_move(move = randomMove,player=game.current_player)

            last_move = randomMove
            pygame.display.flip()

            pygame.time.Clock().tick(FPS)

            screen.fill(WHITE)

        print(winners)
        print(sum(move_times)/len(move_times),"MaxTime",max(move_times),min(move_times))

if __name__ == "__main__":
    main()
