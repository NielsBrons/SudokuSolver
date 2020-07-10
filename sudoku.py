# The Sudoko field
sudoku = [
    [8,6,0,0,0,0,0,0,5],
    [3,1,0,0,9,0,0,0,0],
    [5,2,0,0,1,0,0,9,4],
    [0,7,0,8,0,4,0,0,6],
    [0,0,0,0,0,0,0,0,0],
    [4,0,0,7,0,6,0,8,0],
    [1,3,0,0,6,0,0,4,8],
    [0,0,0,0,7,0,0,2,1],
    [7,0,0,0,0,0,0,5,3]
]

# Print the current Sudoku field
def printBoard(v):
    x = 0
    y = 0
    print(' ___________________________________')
    for i in range(len(sudoku)):
        line = '|'
        for j in range(len(sudoku[i])):
            line = line + ' ' + str(sudoku[i][j]) + ' |'
        print(line)
    print(' -----------------------------------')

# Check if the puzzle is solved
def isSudokuSolved(grid):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False
    return True

# Check if the given value in the give coords is valid on the horizontal
def isHorizontalValid(v, coord):
    x, y = coord
    for i in range(9):
        if sudoku[x][i] == v:
            return False
    return True

# Check if the given value in the give coords is valid on the vertical
def isVerticalValid(v, coord):
    x, y = coord
    for i in range(9):
        if sudoku[i][y] == v:
            return False
    return True

# Check if the given value in the give coords is valid the square
def isSquareValid(v, coord):
    x, y = coord
    # find the 9x9 grid the coord is in
    grid = {'x' : (x // 3) * 3, 'y' : (y // 3) * 3 }
    for i in range(3):
        for j in range(3):
            if sudoku[grid['x']+i][grid['y']+j] == v:
                return False
    return True

# Check if the value is valid in the coord
def isValueValid(v, coord):
    if isHorizontalValid(v, coord) == True and isVerticalValid(v, coord) == True and isSquareValid(v, coord) == True:
        return True
    else:
        return False

def solveSudoku():
    # go through the grid
    for i in range(9):
        for j in range(9):
            # check if the value is empty, if that's the case try numbers
            if sudoku[i][j] == 0:
                # try all possible numbers, starting with 1
                for v in range(1,10):
                    # check if the number is valid
                    if isValueValid(v, (i, j)):
                        # use that number
                        sudoku[i][j] = v
                        # do the same with the next empty field
                        solveSudoku()
                        # if the sudoku is solved return
                        if isSudokuSolved(sudoku):
                            return True
                        # if we couldn't solve the puzzle with the number set the field to 0 and try again with a different number
                        sudoku[i][j] = 0
                return



if __name__ == "__main__":
    solveSudoku()
    printBoard(sudoku)



