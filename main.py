## Prints the board row by row
def printBoard(board):
    for row in board:
        for num in row:
            print(num, end = " ")
        print()

## Checks if value is valid at position on board. Returns True if valid, False if invalid.
def checkValid(board, position, value):
    squareRow, squareCol = position

    # To check the row
    if board[squareRow].count(value) > 0:
        return False

    # To check the col
    for row in board:
        if row[squareCol] == value:
            return False
    
    # To check the box
    boxRow = (squareRow // 3) * 3
    boxCol = (squareCol // 3) * 3
    for row in board[boxRow : boxRow + 3]:
        for number in row[boxCol : boxCol + 3]:
            if number == value:
                return False

    return True

## Returns the (x, y) coordinates of the next 0 in the board. If none found, returns False.
def getNextEmpty(board):
    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == 0:
                return x, y
    return False

## Recursively fills all 0's in the board with valid numbers.
## Returns the completed the board when solved, or False if board cannot be solved.
def solve(board):
    squareToFill = getNextEmpty(board)
    if squareToFill: ## Board is incomplete
        x, y = squareToFill
        ##TODO: Change to pass by value
        newBoard = [*board]

        for i in range(1, 10):
            if checkValid(newBoard, squareToFill, i):
                newBoard[x][y] = i
                nextWorked = solve(newBoard)
                if not nextWorked: ## Check to see if the next step is possible
                    continue
                else:
                    return newBoard
            else:
                continue
        newBoard[x][y] = 0 ## If none of the options worked, go back to the last recursive layer
        return False
    else:
        return board

if __name__ == '__main__':
    easyBoard = [[8, 1, 0, 9, 5, 2, 0, 0, 0],
               [0, 0, 6, 1, 0, 0, 0, 0, 0],
               [0, 2, 5, 0, 4, 7, 0, 0, 0],
               [6, 3, 1, 5, 2, 9, 0, 7, 8],
               [0, 9, 0, 0, 8, 0, 2, 6, 1],
               [2, 0, 0, 7, 0, 0, 3, 0, 0],
               [1, 0, 0, 0, 0, 0, 7, 0, 0],
               [0, 0, 0, 0, 0, 1, 5, 0, 4],
               [7, 5, 8, 3, 0, 4, 0, 9, 2]]

    medBoard =[[0, 3, 0, 0, 7, 0, 0, 4, 0],
               [0, 0, 5, 0, 2, 0, 0, 0, 0],
               [0, 6, 0, 8, 3, 0, 1, 0, 0],
               [4, 0, 0, 0, 8, 0, 0, 3, 6],
               [1, 0, 6, 5, 0, 3, 4, 7, 8],
               [0, 0, 0, 6, 0, 0, 0, 0, 0],
               [0, 0, 4, 0, 6, 0, 0, 1, 0],
               [0, 9, 0, 7, 0, 2, 0, 5, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 3]]

    solved = solve(easyBoard)
    printBoard(solved)