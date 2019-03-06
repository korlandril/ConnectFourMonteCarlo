class OutsideOfBoardError(Exception):
    """Raised when a token is placed outside of game board bounds"""
    pass
class InvalidMoveError(Exception):
    """Raised when a player attempts to make a move that isn't valid"""
    pass

class gameBoard:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.gameBoard = []
        for i in range(row):
            current_row = []
            for j in range(col):
                current_row.append(".")
            self.gameBoard.append(current_row)

    """helper function for the place token"""
    def get_empty_row(self, inputColumn):
        for i in range(self.row):
            if self.gameBoard[0][inputColumn] != ".":
                raise OutsideOfBoardError
            elif i == self.row-1 and self.gameBoard[i][inputColumn] == ".":
                return i
            elif self.gameBoard[i][inputColumn] != ".":
                return i-1

    """places a token on top of the inputted column"""
    def place_token(self, inputToken, inputColumn):
        try:
            empty_row = self.get_empty_row(inputColumn)
            self.gameBoard[empty_row][inputColumn] = inputToken
            print("Token successfully placed")
            self.print_board()
        except OutsideOfBoardError:
            print("Player tried to place a token in a column that is fully filled")
            #raise InvalidMoveError
            pass


    def reset_board(self):
        for i in range(self.row):
            current_row = []
            for j in range(self.col):
                self.gameBoard[i][j] = "."

    #prints the board
    def print_board(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.gameBoard[i][j], end=" ")
            print('\n')

    def check_north(self, input_x, input_y, num_consecutive):
        if input_x == -1 or input_y == -1:
            raise OutsideOfBoardError
        if num_consecutive == 4:
            return True
        else:
            if self.gameBoard[input_x-1][input_y] == self.gameBoard[input_x][input_y]:
                return self.check_north(input_x-1, input_y, num_consecutive + 1)
            else:
                return False

    def check_south(self, input_x, input_y, num_consecutive):
        if input_x == -1 or input_y == -1:
            raise OutsideOfBoardError
        if num_consecutive == 4:
            return True
        else:
            if self.gameBoard[input_x+1][input_y] == self.gameBoard[input_x][input_y]:
                return self.check_south(input_x+1, input_y, num_consecutive + 1)
            else:
                return False

    def check_west(self, input_x, input_y, num_consecutive):
        if input_x == -1 or input_y == -1:
            raise OutsideOfBoardError
        if num_consecutive == 4:
            return True
        else:
            if self.gameBoard[input_x][input_y-1] == self.gameBoard[input_x][input_y]:
                return self.check_west(input_x, input_y-1, num_consecutive + 1)
            else:
                return False

    def check_east(self, input_x, input_y, num_consecutive):
        if input_x == -1 or input_y == -1:
            raise OutsideOfBoardError
        if num_consecutive == 4:
            return True
        else:
            if self.gameBoard[input_x][input_y+1] == self.gameBoard[input_x][input_y]:
                return self.check_east(input_x, input_y+1, num_consecutive + 1)
            else:
                return False

    def check_northwest(self, input_x, input_y, num_consecutive):
        if input_x == -1 or input_y == -1:
            raise OutsideOfBoardError
        if num_consecutive == 4:
            return True
        else:
            if self.gameBoard[input_x-1][input_y-1] == self.gameBoard[input_x][input_y]:
                return self.check_northwest(input_x-1, input_y-1, num_consecutive + 1)
            else:
                return False

    def check_northeast(self, input_x, input_y, num_consecutive):
        if input_x == -1 or input_y == -1:
            raise OutsideOfBoardError
        if num_consecutive == 4:
            return True
        else:
            if self.gameBoard[input_x-1][input_y+1] == self.gameBoard[input_x][input_y]:
                return self.check_northeast(input_x-1, input_y+1, num_consecutive + 1)
            else:
                return False

    def check_southwest(self, input_x, input_y, num_consecutive):
        if input_x == -1 or input_y == -1:
            raise OutsideOfBoardError
        if num_consecutive == 4:
            return True
        else:
            if self.gameBoard[input_x+1][input_y-1] == self.gameBoard[input_x][input_y]:
                return self.check_southwest(input_x+1, input_y-1, num_consecutive + 1)
            else:
                return False

    def check_southeast(self, input_x, input_y, num_consecutive):
        if input_x == -1 or input_y == -1:
            raise OutsideOfBoardError
        if num_consecutive == 4:
            return True
        else:
            if self.gameBoard[input_x+1][input_y+1] == self.gameBoard[input_x][input_y]:
                return self.check_southeast(input_x+1, input_y+1, num_consecutive + 1)
            else:
                return False

    """Check for a Connect Four win condition"""
    def win_check(self):
        for i in range(self.row):
            for j in range(self.col):
                try:
                    if self.gameBoard[i][j] != ".":
                        if (not self.check_north(i, j, 1) or not self.check_south(i, j, 1)
                        or not self.check_west(i, j, 1) or not self.check_east(i, j, 1)
                        or not self.check_northwest(i, j, 1) or not self.check_northeast(i, j, 1)
                        or not self.check_southwest(i, j, 1) or not self.check_southeast(i, j, 1)):
                            return False
                        elif (self.check_north(i, j, 1) or self.check_south(i, j, 1)
                                or self.check_west(i, j, 1) or self.check_east(i, j, 1)
                                or self.check_northwest(i, j, 1) or self.check_northeast(i, j, 1)
                                or self.check_southwest(i, j, 1) or self.check_southeast(i, j, 1)):
                            return True
                    else:
                        continue
                #If a check is performed outside the bounds of the board, move on to the next token
                except IndexError:
                    continue
                #Check for when input_x or input_y decrements to -1
                except OutsideOfBoardError:
                    continue

class Player:
    def __init__(self, playerToken):
        self.player_token = playerToken

    def get_token(self):
        return self.player_token


hello = gameBoard(6, 7)
hello.print_board()
p1 = Player("R")
p2 = Player("Y")

hello.place_token(p1.get_token(), 0)
hello.place_token(p1.get_token(), 0)
hello.place_token(p1.get_token(), 0)
hello.place_token(p1.get_token(), 0)

if hello.win_check():
    print("There is a win!")
else:
    print("No win detected")