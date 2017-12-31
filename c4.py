"""
Connect 4 using 2d arrays
"""


def main():
    """Runs connect 4 game

    2 player game, goes until one wins or the board is full.
    """

    grid = [[0 for j in range(7)] for i in range(6)]
    winstate = 0
    while not winstate:
        for ply in range(1, 3):
            printgrid(grid)
            winstate = ply if getmove(ply, grid) else 0
            if winstate != 0:
                # print("Winstate is", winstate)
                break
            else:
                for rrw in grid:
                    if 0 in rrw:
                        break
                else:
                    winstate = -1
        if winstate:
            break
    printgrid(grid)
    if winstate == -1:
        print("Tie! No one wins")
    else:
        print("Player", winstate, "won!")


def getmove(ply, grid):
    """Gets a player's move

    Asks for input on player ply's move, catches errors, and inserts a coin in selected column. Catches exceptions.

    Arguments:
        ply {integer} -- Whoever's turn it is
        grid {list} -- 2d list (6 rows, 7 columns) representing the board

    Returns:
        boolean -- Whether the player won or not
    """

    while True:
        try:
            winstate = turnandcheck(ply, grid)
            break
        except IndexError:
            print("Column does not exist!")
        except ValueError as err:
            print(err if err == "Column is full!" else "Please input a number!")
        except:
            print("How did you manage to do get this error???")
            raise
    return winstate


def turnandcheck(ply, grid):
    """Gets a player's move

    Asks for input on player ply's move, catches errors, and inserts a coin in selected column. Doesn't catch exceptions.

    Arguments:
        ply {integer} -- Whoever's turn it is
        grid {list} -- 2d list (6 rows, 7 columns) representing the board

    Returns:
        boolean -- Whether the player won or not
    """

    col = int(input("Which column, player " + str(ply) + "? ")) - 1
    dropcoin(grid, col, ply)
    for rowindex in range(6):
        for colindex in range(7):
            if grid[rowindex][colindex] == ply:
                # print(grid[rowindex][colindex])
                if checkwin(grid, rowindex, colindex, ply):
                    return True
    return False


def printgrid(grid):
    """Prints out the grid

    Prints out a nicely formatted grid from a 2d list.

    Arguments:
        grid {list} -- 2d list (6 rows, 7 columns) representing the board
    """

    print("\n1 2 3 4 5 6 7")
    for row in grid:
        print(" ".join(str(j) for j in row))


def dropcoin(grid, col, ply):
    """Drops a coin in column col

    Attempts to drop a coin in column col, raises ValueError if column is full.

    Arguments:
        grid {list} -- 2d list (6 rows, 7 columns) representing the board
        col {int} -- Index of column where coin is to be dropped
        ply {int} -- Player whose number will be on the coin

    Raises:
        ValueError -- This will be raised if the selected column is full
    """

    if grid[0][col] != 0:
        raise ValueError("Column is full!")
    if grid[5][col] == 0:
        grid[5][col] = ply
        return
    rowindex = 0
    while grid[rowindex][col] == 0:
        rowindex += 1
    grid[rowindex - 1][col] = ply


def checkwin(grid, row, col, ply):
    """Check if a player has connected 4 starting from a point

    Used to check if a player has won, if pointed at the beginning of a line of 4 this should return True.

    Arguments:
        grid {list} -- 2d list (6 rows, 7 columns) representing the board
        row {int} -- Index of row to target
        col {int} -- Index of column to target
        ply {int} -- Player to check win for

    Returns:
        boolean -- True if player ply has connected 4 starting on (row,col) o/w False
    """

    for rowdiff in range(-1, 2):
        for coldiff in range(-1, 2):
            if not ((rowdiff == 0 and coldiff == 0) or row + rowdiff * 3 < 0 or col + coldiff * 3 < 0):
                try:
                    for i in range(1, 4):
                        # print("Found", grid[row + rowdiff * i][col + coldiff * i], "at", row + rowdiff * i, ",", col + coldiff * i)
                        if grid[row + rowdiff * i][col + coldiff * i] != ply:
                            # print("No match found going", rowdiff, coldiff)
                            break
                    else:
                        # print("Match found going", rowdiff, coldiff)
                        return True
                except IndexError:
                    pass
    return False


if __name__ == "__main__":
    main()
