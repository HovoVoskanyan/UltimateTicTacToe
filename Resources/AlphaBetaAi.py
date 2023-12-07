class AlphaBetaAi:
    def __init__(self, player,maximizer,minimizer):
        self.player = player
        self.maximizer = maximizer
        self.minimizer = minimizer


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

    def alpha_beta_recursive(self,game, depth, alpha, beta, maximizing_player, last_move):
        current_state_eval = self.evaluate(game)

        if depth == 0 or game.is_game_over():
            return current_state_eval

        moves = game.get_available_moves(last_move)

        if maximizing_player == 1:
            max_eval = float('-inf')
            for move in moves:
                cloned_game = game.clone()
                cloned_game.make_move(move, 1)
                eval = self.alpha_beta_recursive(cloned_game, depth - 1, alpha, beta, self.minimizer, move)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if max_eval > beta:
                    break  # Beta cut-off

            return max_eval
        else:
            min_eval = float('inf')
            for move in moves:
                cloned_game = game.clone()
                cloned_game.make_move(move, 2)  # Assuming "O" is the minimizing player

                eval = self.alpha_beta_recursive(cloned_game, depth - 1, alpha, beta, self.maximizer, move)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if min_eval < alpha:
                    break  # Alpha cut-off

            return min_eval

    def find_best_move_alpha_beta(self,game, depth=3, last_move=None):
        alpha = float('-inf')
        beta = float('inf')
        maximizing_player = 1  # Assuming player 1 is the maximizing player

        available_moves = game.get_available_moves(last_move)
        best_move = None
        best_eval = 0
        if self.maximizer == self.player:
            best_eval = float('-inf')
        else:
            best_eval = float('+inf')

        for move in available_moves:
            new_game = game.clone()
            new_game.make_move(move, self.player)
            eval = self.alpha_beta_recursive(new_game,depth,alpha,beta,self.player,last_move=move)
            if self.maximizer == self.player:
                if eval > best_eval:
                    best_eval = eval
                    best_move = move
            else:
                if eval < best_eval:
                    best_eval = eval
                    best_move = move


        return best_move
