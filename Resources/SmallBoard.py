class SmallBoard:
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        """Make a move on the small board for the specified player."""
        if self.board[row][col] == 0:
            self.board[row][col] = player
            return True  # Move successful
        else:
            return False  # Cell already occupied

    def check_winner(self):
        # Check rows
        for row in self.board:
            if all(cell == row[0] and cell != 0 for cell in row):
                return row[0]

        # Check columns
        for col in range(3):
            if all(self.board[row][col] == self.board[0][col] and self.board[row][col] != 0 for row in range(3)):
                return self.board[0][col]

        # Check diagonals
        if all(self.board[i][i] == self.board[0][0] and self.board[i][i] != 0 for i in range(3)) or \
                all(self.board[i][2 - i] == self.board[0][2] and self.board[i][2 - i] != 0 for i in range(3)):
            return self.board[1][1]

        # No winner
        return None
