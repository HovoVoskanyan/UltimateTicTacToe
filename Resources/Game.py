import time
import random
from Resources.BigBoard import BigBoard


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

    def random_move(self):
        available_moves = self.get_available_moves()
        if available_moves:
            return random.choice(available_moves)
        else:
            return None  # No available moves
    def get_available_moves(self):
        moves = []
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
def monte_carlo(game, player, iterations=1000):
    start_time = time.time()

    def simulate_random_game(game):
        while not game.is_game_over():
            moves = game.get_available_moves()
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

    moves = game.get_available_moves()
    scores = {move: 0 for move in moves}

    for _ in range(iterations):
        move = random.choice(moves)

        cloned_game = game.clone()  # Implement a clone method in your Game class
        cloned_game.make_move(move, player)
        result = simulate_random_game(cloned_game)
        scores[move] += result

    best_move = max(scores, key=scores.get)
    end_time = time.time()
    time_taken = end_time - start_time

    return best_move, time_taken

# MiniMax Algorithm
def minimax(game, depth, maximizing_player):
    start_time = time.time()

    def evaluate(game):
        # Your implementation of a heuristic evaluation function goes here
        pass

    def minimax_recursive(game, depth, maximizing_player):
        if depth == 0 or game.is_game_over():
            return evaluate(game)

        if maximizing_player:
            max_eval = float('-inf')
            for move in game.get_available_moves():
                cloned_game = game.clone()  # Implement a clone method in your Game class
                cloned_game.make_move(move, "X")  # Assuming "X" is the maximizing player
                eval = minimax_recursive(cloned_game, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in game.get_available_moves():
                cloned_game = game.clone()
                cloned_game.make_move(move, "O")  # Assuming "O" is the minimizing player
                eval = minimax_recursive(cloned_game, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    moves = game.get_available_moves()
    best_move = max(moves, key=lambda move: minimax_recursive(game, depth, False))

    end_time = time.time()
    time_taken = end_time - start_time

    return best_move, time_taken

# Alpha-Beta Pruning Algorithm
def alpha_beta_pruning(game, depth, alpha, beta, maximizing_player):
    start_time = time.time()

    def evaluate(game):
        # Your implementation of a heuristic evaluation function goes here
        pass

    def alpha_beta_recursive(game, depth, alpha, beta, maximizing_player):
        if depth == 0 or game.is_game_over():
            return evaluate(game)

        moves = game.get_available_moves()

        if maximizing_player:
            max_eval = float('-inf')
            for move in moves:
                cloned_game = game.clone()
                cloned_game.make_move(move, "X")  # Assuming "X" is the maximizing player
                eval = alpha_beta_recursive(cloned_game, depth - 1, alpha, beta, False)
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
                eval = alpha_beta_recursive(cloned_game, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    moves = game.get_available_moves()
    best_move = max(moves, key=lambda move: alpha_beta_recursive(game, depth, alpha, beta, False))

    end_time = time.time()
    time_taken = end_time - start_time

    return best_move, time_taken
