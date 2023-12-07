class MinimaxAI:
    def __init__(self, player, maximizer, minimizer):
        self.player = player
        self.maximizer = maximizer
        self.minimizer = minimizer

    def evaluate(self,game):
        # Check if the game is won by either player
        winner = game.big_board.check_winner()
        if winner == self.maximizer:
            return 100  # Player 1 (X) wins
        elif winner == self.minimizer:
            return -100  # Player 2 (O) wins

        player1_lines = game.big_board.count_winning_lines(self.maximizer)
        player2_lines = game.big_board.count_winning_lines(self.minimizer)

        score = player1_lines - player2_lines

        return score


    def minimax(self, game, depth, current_player,last_move = None):
        current_state_eval = self.evaluate(game)

        if depth == 0 or game.is_game_over():
            return self.evaluate(game)

        available_moves = game.get_available_moves(last_move)

        if current_player == self.maximizer:
            max_eval = float('-inf')
            for move in available_moves:
                new_game = game.clone()
                new_game.make_move(move, self.maximizer)
                eval = self.minimax(new_game, depth - 1, self.minimizer,last_move = move)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in available_moves:
                new_game = game.clone()
                new_game.make_move(move, self.minimizer)
                eval = self.minimax(new_game, depth - 1, self.maximizer,last_move = move)
                min_eval = min(min_eval, eval)
            return min_eval


    def find_best_move(self, game, depth=3,last_move =None):
        available_moves = game.get_available_moves(last_move)
        best_move = None
        if self.maximizer == self.player:
            best_eval = float('-inf')
        else:
            best_eval = float('+inf')
        for move in available_moves:
            new_game = game.clone()
            new_game.make_move(move, self.player)
            eval = self.minimax(new_game, depth, self.player, last_move= move )
            if self.maximizer == self.player:
                if eval > best_eval:
                    best_eval = eval
                    best_move = move
            else:
                if eval < best_eval:
                    best_eval = eval
                    best_move = move

        return best_move
