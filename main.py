# Function to display the Tic Tac Toe board
def display_board(small_board,ultimate_board ):
    print(f"Printing Ultimate board")

    for i in range(len(ultimate_board)):
        if i % 3 == 0 and i > 0:
            print("-" * 21)
        for j in range(len(ultimate_board[i])):
            if j % 3 == 0 and j > 0:
                print("|", end=" ")  # Separator for every three columns

            if ultimate_board[i][j] == 0:
                print("*", end=" ")
            elif ultimate_board[i][j] == 1:
                print("X", end=" ")
            elif ultimate_board[i][j] == 2:
                print("O", end=" ")
        print()

    print(f"\nPrinting small board \n")

    for i in range(len(small_board)):
        print("-" * 10,end="\n")  # Separator line for every three rows
        for j in range(len(small_board[i])):
            print("|", end="")  # Separator for every three columns

            if small_board[i][j] == 0:
                print("*", end=" ")

            elif small_board[i][j] == 1:
                print("X", end=" ")

            elif small_board[i][j] == 2:
                print("O", end=" ")
            if(j==len(small_board[i])-1):
                print("|", end="")  # Separator for every three columns
        print()
        if (i == len(small_board) - 1):
            print("-" * 10, end="\n")  # Separator line for every three rows
def main():

    ultimate_board_example = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    small_board_example = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    display_board(small_board_example,ultimate_board_example)


if __name__ == "__main__":
    main()
