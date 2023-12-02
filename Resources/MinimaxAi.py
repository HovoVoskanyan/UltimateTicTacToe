class MinimaxAI:
    def __init__(self, player):
        self.player = player


    def evaluate(self,game):
        # Check if the game is won by either player
        winner = game.big_board.check_winner()
        if winner == 1:
            return 100  # Player 1 (X) wins
        elif winner == 2:
            return -100  # Player 2 (O) wins

        player1_lines = game.big_board.count_winning_lines(1)
        player2_lines = game.big_board.count_winning_lines(2)

        score = player1_lines - player2_lines

        return score


    def minimax(self, game, depth, maximizing_player,last_move = None):
        if depth == 0 or game.is_game_over():
            return self.evaluate(game)

        available_moves = game.get_available_moves(last_move)

        if maximizing_player:
            max_eval = float('-inf')
            for move in available_moves:
                new_game = game.clone()
                new_game.make_move(move, self.player)
                eval = self.minimax(new_game, depth - 1, 2,last_move = move)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in available_moves:
                new_game = game.clone()
                new_game.make_move(move, 3 - self.player)  # Switch player
                eval = self.minimax(new_game, depth - 1, 1,last_move = move)
                min_eval = min(min_eval, eval)
            return min_eval


    def find_best_move(self, game, depth=3,last_move =None):
        available_moves = game.get_available_moves(last_move)
        best_move = None
        best_eval = float('-inf')

        for move in available_moves:
            new_game = game.clone()
            new_game.make_move(move, self.player)
            eval = self.minimax(new_game, depth - 1, self.player, last_move= move )
            print(best_move)
            if eval > best_eval:
                best_eval = eval
                best_move = move

        return best_move
