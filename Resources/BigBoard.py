from Resources.SmallBoard import SmallBoard
class BigBoard:
    def __init__(self):
        self.board = [[SmallBoard() for _ in range(3)] for _ in range(3)]

    def count_winning_lines(self, player):
        count = 0
        for i in range(3):
            # Check rows
            for j in range(3):
                if(self.board[i][j].is_winner(player)):
                    count += 1

                if (self.board[j][i].is_winner(player)):
                    count += 1

        # Check diagonals
        if self.board[i][i].is_winner(player):
            count += 1

        if self.board[i][2 - i].is_winner(player):
            count += 1

        return count
    def make_move(self, ultimate_row, ultimate_col, small_row, small_col, player):
        """Make a move on the big board, specifying both the ultimate and small board coordinates."""
        return self.board[ultimate_row][ultimate_col].make_move(small_row, small_col, player)

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
            first_cell_winner = row[0].check_winner()
            if all(small_board.check_winner() == first_cell_winner and first_cell_winner != 0 for small_board in
                   row):
                if first_cell_winner != 0 or first_cell_winner != None:
                    return first_cell_winner

        # Check columns
        for col in range(3):
            first_cell_winner = self.board[0][col].check_winner()
            if all(self.board[row][col].check_winner() == first_cell_winner and first_cell_winner!=0 for row in
                   range(3)):
                if first_cell_winner != 0 or first_cell_winner != None:
                    return first_cell_winner

        # Check diagonals
        diagonal1_winner = self.board[0][0].check_winner()
        diagonal2_winner = self.board[0][2].check_winner()

        if all(self.board[i][i].check_winner() == diagonal1_winner and diagonal1_winner!=0 for i in
               range(3)) or \
                all(self.board[i][2 - i].check_winner() == diagonal2_winner and diagonal2_winner!=-0 for i in
                    range(3)):
            if diagonal1_winner != 0 or diagonal1_winner != None:
                return diagonal1_winner

        # No winner
        return None