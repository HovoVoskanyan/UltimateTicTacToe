class SmallBoard:
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]

    def is_winner(self, player):
        # Check rows
        for row in self.board:
            if all(mark == player for mark in row):
                return True

        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)):
            return True

        if all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False
    def make_move(self, row, col, player):
        if self.board[row][col] == 0:
            self.board[row][col] = player
            return True
        else:
            return False
    def check_winner(self):
        # Check row
        for row in self.board:
            is_winner_row = True
            for cell in row:
                if(row[0] != cell):
                    is_winner_row = False
            if(is_winner_row):
                return row[0]



        # Check columns
        for col in range(3):
            if all(self.board[row][col] == self.board[0][col] and self.board[row][col] != 0 for row in range(3)):
                return self.board[0][col]

        # Check diagonals
        if all(self.board[i][i] == self.board[0][0] and self.board[i][i] != 0 for i in range(3)) or \
                all(self.board[i][2 - i] == self.board[0][2] and self.board[i][2 - i] != 0 for i in range(3)):
            return self.board[1][1]

        return 0
