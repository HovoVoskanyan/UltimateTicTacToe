import time
import random
from Resources.BigBoard import BigBoard
from Resources.MinimaxAi import MinimaxAI
from  Resources.AlphaBetaAi import AlphaBetaAi


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
        if(move is None):
            return
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
                small_board = self.big_board.board[ultimate_row][ultimate_col]
                is_won = small_board.is_winner(1) | small_board.is_winner(2)
                if is_won:
                    continue
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

    ai = MinimaxAI(player=maximizing_player,maximizer=1,minimizer=2)
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

    score = player1_lines - player2_lines

    return score


def alpha_beta(game, depth, maximizing_player,last_move):
    start_time = time.time()

    ai = AlphaBetaAi(player=maximizing_player,maximizer =1,minimizer=2)
    best_move = ai.find_best_move_alpha_beta(game,3,last_move)

    end_time = time.time()
    time_taken = end_time - start_time

    return best_move, time_taken
