def winning_combos(arr, char):
    combos = [
        [(1,1), (1,2), (1,3)], [(2,1), (2,2), (2,3)], [(3,1), (3,2), (3,3)], #Solutions for rows
        [(1,1), (2,1), (3,1)], [(1,2), (2,2), (3,2)], [(1,3), (2,3), (3,3)], #Solutions for Columns
        [(1,3), (2,2), (3,1)], [(1,1), (2,2), (3,3)] #Solution for diagonals
    ]
    #Checks wins 
    for combo in winning_combos:
        if all(arr[row-1][col-1] == char for row, col in combo):
            return True
    return False


def main():

    print("Select the board size:")
    print("small. 3x3")
    print("medium. 4x4")
    print("large. 5x5")
    choice = int(input("Enter your choice (small, medium, large): "))

    small = rows,columns(3) 
    medium = rows,columns(4) 
    large = rows,columns(5) 
    if choice == small:
        rows, columns = 3, 3
    elif choice == medium:
        rows, columns = 4, 4
    elif choice == large:
        rows, columns = 5, 5
    else:
        print("Invalid choice. Try again")
        rows, columns = 3, 3

    # Initialize an empty board
    board = [[' ' for _ in range(columns)] for _ in range(rows)]

    # Ask the user to input X or O
    for i in range(3):
        for j in range(3):
            board[i][j] = input("Enter 'X' or 'O' for position ({}, {}): ".format(i+1, j+1))

    # Print the board
    print("Current board:")
    for row in board:
        print(' '.join(row))

if __name__ == "__main__":
    main()
 