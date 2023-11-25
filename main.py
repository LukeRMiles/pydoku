from time import sleep
def printBoard(board):
    for row in board:
        for num in row:
            print(num, end = " ")
        print()

def checkValid(board, square):
    ## Board in form [[]x9], square is tuple coordinates
    ## Returns True if square is valid, false if square in invalid
    squareRow, squareCol = square
    valueToCheck = board[squareRow][squareCol]
    ## Check row
    if (board[squareRow].count(valueToCheck) > 1):
        ## Check to see if there are more than 1 of that value on the row
        return False
    ## Check col
    for i, row in enumerate(board):
        if (row[squareCol] == valueToCheck) and (i != squareRow):
            ## If squares have same value and is not the square we're checking
            return False
    ## Check square
    startingRow = (squareRow // 3) * 3
    startingCol = (squareCol // 3) * 3
    vals = []
    for row in board[startingRow:startingRow + 3]:
        for value in row[startingCol:startingCol + 3]:
            ## Get all the values in the square and add them to an array
            vals.append(value)
    if vals.count(valueToCheck) > 1:
        ## Check to see if the value appears more than once
        ## If it does, the value is invalid and return False
        ## Otherwise, return true
        return False
    return True ## End condition

def solve(board):
    ## Returns a board ([[]x9]) if successful, false if not
    def getNextEmpty():
        for x, row in enumerate(board):
            for y, value in enumerate(row):
                if value == 0:
                    return x, y
        return False

    squareToFill = getNextEmpty()
    if squareToFill: ## Board is incomplete
        x, y = squareToFill
        for i in range(1, 10):
            ## TODO: Change the checkValid() call to checkValid(newBoard, i) to
            ## reduce the number of unnecessary changes (putting a 5 next to a 5)
            sleep(0.01)
            newBoard = [*board] ## To avoid pass by reference
            newBoard[x][y] = i
            printBoard(newBoard)
            print("\n")
            if checkValid(newBoard, squareToFill):
                ## If value is valid, go to the next zero
                nextWorked = solve(newBoard)
                if nextWorked == False:
                    ## Next value didn't find anything
                    continue ## to next number
                else:
                    ## Next value found something, solved?
                    return newBoard
            else:
                ## If value is invalid, try the next value
                continue ## to next number
        ## All the values are invalid
        board[x][y] = 0
        return False
    else:
        ## Board is complete
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

    solved = solve(medBoard)