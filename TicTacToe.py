import time

class Board():
    def __init__(self):
        self.marked = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.grid = self.make_grid()

    def make_grid(self):
        grid = []
        l = self.marked
        for i in range(3):
            row = [l[0+(i*3)], l[1+(i*3)], l[2+(i*3)]]
            grid.append(row)
        return grid

    def update_board(self, row, col, sign):
        spot = (int(row)-1)*3 + (int(col)-1)
        self.marked[spot] = str(sign)
        self.grid = self.make_grid()

    def draw(self):
        grid = self.grid
        for i in range(3):
            print("{}|{}|{}".format(grid[i][0], grid[i][1], grid[i][2]))


    def win(self):
        grid = self.grid
        havewinner = False
        tie = True
        winner = 0
        for i in range(3):
            if grid[i][0] == grid[i][1] == grid[i][2] != " ": # hori win
                winner = grid[i][0]
                havewinner = True
            elif grid[0][i] == grid[1][i] == grid[2][i] != " ": # verti win
                winner = grid[0][i]
                havewinner = True
            elif grid[0][0] == grid[1][1] == grid[2][2] != " ":
                winner = grid[0][0]
                havewinner = True
            elif grid[0][2] == grid[1][1] == grid[2][0] != " ":
                winner = grid[0][2]
                havewinner = True

            for j in range(3):
                if grid[i][j] == " ":
                    tie = False

        if tie:
            return 3
        elif not havewinner:
            return havewinner
        else:
            if winner == "X":
                return 1
            else:
                return 2

def inputting(name):
    v = input("Enter a {} (1-3): ".format(name))
    while not is_int(v):
        print("READ! IT'S 1 to 3")
        v = input("Enter a {} (1-3): ".format(name))
    else:
        while not 0 < int(v) < 4:
            print("READ! IT'S 1 to 3")
            v = input("Enter a {} (1-3): ".format(name))
        else:
            return v

def check_inputs(marked, row, col):
    spot = (int(row) - 1) * 3 + (int(col) - 1)
    if marked[spot] == " ":
        return True
    else:
        return False

rounds = 0
def turn():
    global rounds
    if rounds % 2 == 0:
        p = 1
    else:
        p = 2
    rounds += 1

    return p

def is_int(n):
    try:
        n = int(n)
        return True
    except ValueError:
        return False

def main():
    board = Board()
    while not board.win():
        p_turn = turn()
        if p_turn == 1:
            s = "X"
        else:
            s = "O"

        print("It is Player {}'s turn".format(p_turn))
        row = inputting("row")
        col = inputting("column")
        while not check_inputs(board.marked, row, col):
            print("Spot Already Marked")
            row = inputting("row")
            col = inputting("column")
        else:
            board.update_board(row, col, s)
            board.draw()
    else:
        wnum = board.win()
        if wnum == 3:
            print("Tied game!")
        else:
            print("Player {} won!".format(wnum))
        time.sleep(3)


main()