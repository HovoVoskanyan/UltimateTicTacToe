from Resources.SmallBoard import SmallBoard
class BigBoard:
    def __init__(self):
        self.board = [[SmallBoard() for _ in range(3)] for _ in range(3)]

    def make_move(self, ultimate_row, ultimate_col, small_row, small_col, player):
        """Make a move on the big board, specifying both the ultimate and small board coordinates."""
        return self.board[ultimate_row][ultimate_col].make_move(small_row, small_col, player)

    def get_available_moves(self):
        moves = []
        for ultimate_row in range(3):
            for ultimate_col in range(3):
                small_board = self.board[ultimate_row][ultimate_col]
                for small_row in range(3):
                    for small_col in range(3):
                        if small_board.board[small_row][small_col] == 0:
                            moves.append((ultimate_row, ultimate_col, small_row, small_col))
        return moves

    def visualize(self):
        """Visualize the big board."""
        visualization = [[0 for _ in range(9)] for _ in range(9)]

        for ultimate_row in range(3):
            for ultimate_col in range(3):
                for row in range(3):
                    for col in range(3):
                        small_board_value = self.board[ultimate_row][ultimate_col].board[row][col]
                        if small_board_value == 1:
                            visualization[ultimate_row * 3 + row][ultimate_col * 3 + col] = 1
                        elif small_board_value == 2:
                            visualization[ultimate_row * 3 + row][ultimate_col * 3 + col] = 2
                        else:
                            visualization[ultimate_row * 3 + row][ultimate_col * 3 + col] = 0
        return visualization

    def check_winner(self):
        # Check rows
        for row in self.board:
            if all(small_board.check_winner() == row[0].check_winner() and row[0].check_winner() is not None for
                   small_board in row):
                return row[0].check_winner()

        # Check columns
        for col in range(3):
            if all(self.board[row][col].check_winner() == self.board[0][col].check_winner() and self.board[0][
                col].check_winner() is not None for row in range(3)):
                return self.board[0][col].check_winner()

        # Check diagonals
        if all(self.board[i][i].check_winner() == self.board[0][0].check_winner() and self.board[0][
            0].check_winner() is not None for i in range(3)) or \
                all(self.board[i][2 - i].check_winner() == self.board[0][2].check_winner() and self.board[0][
                    2].check_winner() is not None for i in range(3)):
            return self.board[1][1].check_winner()

        # No winner
        return None