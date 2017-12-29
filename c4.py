"""
Connect 4 using 2d arrays
"""

def main():
    """Runs the game."""
    grid = [[0 for j in range(7)] for i in range(6)]
    winstate = 0
    while not winstate:
        for i in range(1, 3):
            print()
            printgrid(grid)
            while True:
                try:
                    col = int(input("Which column, player " + str(i) + "? "))-1
                    row = dropcoin(grid, col, i)
                    winstate = checkwin(grid, row, col)
                    break
                except IndexError:
                    print("Column does not exist!")
                except ValueError as err:
                    print(err)
                except:
                    print("How did you manage to do get this error???")
                    raise
            for rrw in grid:
                if 0 in rrw:
                    break
            else:
                winstate = -1
            if winstate:
                break
    print()
    printgrid(grid)
    print("Player ", winstate, " won!")

def printgrid(grid):
    """Prints out grid readably (for user)."""
    print("1 2 3 4 5 6 7")
    for row in grid:
        print(" ".join(str(j) for j in row))

def dropcoin(grid, col, ply):
    """Attempts to drop a coin in the grid. Raises ValueError if not possible."""
    if grid[0][col] != 0:
        raise ValueError("Column is full!")
    if grid[5][col] == 0:
        grid[5][col] = ply
        return 5
    rowindex = 0
    while grid[rowindex][col] == 0:
        rowindex += 1
    grid[rowindex-1][col] = ply
    return rowindex - 1

def checkwin(grid, row, col):
    """Returns a number if it has won starting on the row,col inputs, o/w 0"""
    startnum = grid[row][col]
    for rowdiff in range(-1, 2):
        for coldiff in range(-1, 2):
            if not (rowdiff == 0 and coldiff == 0):
                try:
                    for i in range(1, 4):
                        if grid[row + rowdiff * i][col + coldiff * i] != startnum:
                            break
                    else:
                        return startnum
                except IndexError:
                    pass
    return 0

if __name__ == "__main__":
    main()
