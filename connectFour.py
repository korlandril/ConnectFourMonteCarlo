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
            if i == self.row-1 and self.gameBoard[i][inputColumn] == ".":
                return i
            elif self.gameBoard[i][inputColumn] != ".":
                return i-1

    """places a token on top of the inputted column"""
    def placeToken(self, inputToken, inputColumn):
        empty_row = self.get_empty_row(inputColumn)
        self.gameBoard[empty_row][inputColumn] = inputToken
        print("Token successfully placed")
        self.print_board()



    #prints the board
    def print_board(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.gameBoard[i][j], end=" ")
            print('\n')


class Player:
    def __init__(self, playerToken):
        self.playerToken = playerToken


hello = gameBoard(6, 7)
hello.print_board()
hello.placeToken("h",0)
hello.placeToken("j",0)
hello.placeToken("h",0)
hello.placeToken("j",0)
hello.placeToken("j",4)
hello.placeToken("h",3)
hello.placeToken("j",3)
hello.placeToken("j",0)
