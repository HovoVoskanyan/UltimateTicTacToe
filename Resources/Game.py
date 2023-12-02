import time
import random
from Resources.BigBoard import BigBoard
from Resources.MinimaxAi import MinimaxAI


class Game:
    def __init__(self):
        self.big_board = BigBoard()
        self.current_player = 1

    def switch_player(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player =1

    def make_move(self, move, player):
        if(self.current_player ==2):
            a =5
        self.big_board.make_move(move[0], move[1], move[2], move[3], player)
        self.switch_player()

    def is_game_over(self):
        return self.big_board.check_winner() or not self.get_available_moves()

    def random_move(self,last_move):
        available_moves = self.get_available_moves(last_move)
        if available_moves:
            return random.choice(available_moves)
        else:
            return None  # No available moves
    def get_available_moves(self, last_move=None):
        moves = []

        # If no move has been made yet, allow the first player to place their move anywhere
        if not last_move :
            for ultimate_row in range(3):
                for ultimate_col in range(3):
                    for small_row in range(3):
                        for small_col in range(3):
                            if self.big_board.board[ultimate_row][ultimate_col].board[small_row][small_col] == 0:
                                moves.append((ultimate_row, ultimate_col, small_row, small_col))
            return moves

        # If a move has been made, find the last move's corresponding 3x3 grid
        if last_move:
            _,_,ultimate_row, ultimate_col = last_move

            # If the corresponding 3x3 grid is not won or full, allow the current player to place their move there
            if (
                    not self.big_board.board[ultimate_row][ultimate_col].check_winner()
                    and not all(
                all(cell != 0 for cell in row)
                for row in self.big_board.board[ultimate_row][ultimate_col].board
            )
            ):
                for small_row in range(3):
                    for small_col in range(3):
                        if self.big_board.board[ultimate_row][ultimate_col].board[small_row][small_col] == 0:
                            moves.append((ultimate_row, ultimate_col, small_row, small_col))
                return moves

        # If the corresponding 3x3 grid is won or full, allow the current player to place their move anywhere on the entire board
        for ultimate_row in range(3):
            for ultimate_col in range(3):
                for small_row in range(3):
                    for small_col in range(3):
                        if self.big_board.board[ultimate_row][ultimate_col].board[small_row][small_col] == 0:
                            moves.append((ultimate_row, ultimate_col, small_row, small_col))
        return moves
    def clone(self):
        new_game = Game()
        new_game.big_board = BigBoard()
        for ultimate_row in range(3):
            for ultimate_col in range(3):
                for row in range(3):
                    for col in range(3):
                        small_board_value = self.big_board.board[ultimate_row][ultimate_col].board[row][col]
                        new_game.big_board.board[ultimate_row][ultimate_col].board[row][col] = small_board_value
        new_game.current_player = self.current_player
        return new_game

    # Monte Carlo Algorithm
def monte_carlo(game, player, iterations=1000,last_move = None):
    start_time = time.time()

    def simulate_random_game(game,last_move_sim):

        random_move = last_move_sim

        while not game.is_game_over():
            moves = game.get_available_moves(random_move)
            if not moves:
                break
            random_move = random.choice(moves)
            game.make_move(random_move, game.current_player)
        winner = game.big_board.check_winner()
        if winner == 1:
            return 1  # Player 'X' wins
        elif winner == 2:
            return -1  # Player 'O' wins
        else:
            return 0  # It's a draw
        pass

    moves = game.get_available_moves(last_move)
    scores = {move: 0 for move in moves}

    for _ in range(iterations):
        move = random.choice(moves)

        cloned_game = game.clone()  # Implement a clone method in your Game class
        cloned_game.make_move(move, player)
        result = simulate_random_game(cloned_game,move)
        scores[move] += result

    best_move = max(scores, key=scores.get)
    end_time = time.time()
    time_taken = end_time - start_time

    return best_move, time_taken

# MiniMax Algorithm
def minimax(game, depth, maximizing_player,last_move):
    start_time = time.time()

    ai = MinimaxAI(player=1)
    best_move = ai.find_best_move(game,3,last_move)

    end_time = time.time()
    time_taken = end_time - start_time

    return best_move, time_taken

# Alpha-Beta Pruning Algorithm


def evaluate(game):
    winner = game.big_board.check_winner()
    if winner == 1:
        return 100  # Player 1 (X) wins
    elif winner == 2:
        return -100  # Player 2 (O) wins

    player1_lines = game.big_board.count_winning_lines(1)
    player2_lines = game.big_board.count_winning_lines(2)

    player1_small_boards = sum(
        1 for row in game.big_board.board for small_board in row if small_board.check_winner() == 1
    )
    player2_small_boards = sum(
        1 for row in game.big_board.board for small_board in row if small_board.check_winner() == 2
    )

    # Add more factors as needed
    score = (player1_lines + player1_small_boards) - (player2_lines + player2_small_boards)

    return score

def alpha_beta_recursive(game, depth, alpha, beta, maximizing_player,last_move):
    if depth == 0 or game.is_game_over():
        return evaluate(game)

    moves = game.get_available_moves(last_move)

    if maximizing_player==1:
        max_eval = float('-inf')
        for move in moves:
            cloned_game = game.clone()
            cloned_game.make_move(move, "X")  # Assuming "X" is the maximizing player
            eval = alpha_beta_recursive(cloned_game, depth - 1, alpha, beta, 2,move)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in moves:
            cloned_game = game.clone()
            cloned_game.make_move(move, "O")  # Assuming "O" is the minimizing player
            eval = alpha_beta_recursive(cloned_game, depth - 1, alpha, beta, 1,move)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval



def find_best_move_alpha_beta(game, depth=3, last_move= None):
    start_time = time.time()
    alpha = float('-inf')
    beta = float('inf')
    maximizing_player = 1  # Assuming player 1 is the maximizing player

    moves = game.get_available_moves(last_move)

    best_move = max(
        moves,
        key=lambda move: alpha_beta_recursive(game, depth, alpha, beta, maximizing_player, last_move=move)
    )

    end_time = time.time()
    time_taken = end_time - start_time

    return best_move, time_taken