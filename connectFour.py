from copy import deepcopy
import random
import math

NUM_SIMULATIONS_P1 = 75
NUM_SIMULATIONS_P2 = 50

"""Raised when attempting to iterate outside of the bounds of the game board"""
class OutsideOfBoardError(Exception):
    """Raised when a token is placed outside of game board bounds"""
    pass

"""Raised when attempting to place a token in a column that is fully filled"""
class InvalidMoveError(Exception):
    """Raised when a player attempts to make a move that isn't valid"""
    pass

"""State class for the game board"""
class gameBoardState:
    def __init__(self, row, col, inputPlayer1, input_board = None):
        self.row = row
        self.col = col
        self.payout_score = 0.0
        self.local_samples = 0
        self.player1 = inputPlayer1

        self.gameBoard = []

        """The state class can either be instantiated with an inputted board or a blank one will be created"""
        if input_board is None:
            for i in range(row):
                current_row = []
                for j in range(col):
                    current_row.append(".")
                self.gameBoard.append(current_row)
            self.winner = "No_winner"
        else:
            self.gameBoard = input_board


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
           #print("Token successfully placed")
            #self.print_board()
        except OutsideOfBoardError:
            #print("Player tried to place a token in a column that is fully filled")
            raise InvalidMoveError
            #pass

    """Clears all tokens on the board"""
    def reset_board(self):
        for i in range(self.row):
            current_row = []
            for j in range(self.col):
                self.gameBoard[i][j] = "."

    """prints the board"""
    def print_board(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.gameBoard[i][j], end=" ")
            print('\n')

    #####################################################################################
    """Directional checks for four of the same token in all eight directions."""
    def check_north(self, input_x, input_y, num_consecutive):
        try:
            if input_x == -1 or input_y == -1:
                raise OutsideOfBoardError
            if num_consecutive == 4:
                return True
            else:
                if self.gameBoard[input_x-1][input_y] == self.gameBoard[input_x][input_y]:
                    return self.check_north(input_x-1, input_y, num_consecutive + 1)
                else:
                    return False
        except IndexError:
            return False

    def check_south(self, input_x, input_y, num_consecutive):
        try:
            if input_x == -1 or input_y == -1:
                raise OutsideOfBoardError
            if num_consecutive == 4:
                return True
            else:
                if self.gameBoard[input_x+1][input_y] == self.gameBoard[input_x][input_y]:
                    return self.check_south(input_x+1, input_y, num_consecutive + 1)
                else:
                    return
        except IndexError:
            return False

    def check_west(self, input_x, input_y, num_consecutive):
        try:
            if input_x == -1 or input_y == -1:
                raise OutsideOfBoardError
            if num_consecutive == 4:
                return True
            else:
                if self.gameBoard[input_x][input_y-1] == self.gameBoard[input_x][input_y]:
                    return self.check_west(input_x, input_y-1, num_consecutive + 1)
                else:
                    return False
        except IndexError:
            return False

    def check_east(self, input_x, input_y, num_consecutive):
        try:
            if input_x == -1 or input_y == -1:
                raise OutsideOfBoardError
            if num_consecutive == 4:
                return True
            else:
                if self.gameBoard[input_x][input_y+1] == self.gameBoard[input_x][input_y]:
                    return self.check_east(input_x, input_y+1, num_consecutive + 1)
                else:
                    return False
        except IndexError:
            return False

    def check_northwest(self, input_x, input_y, num_consecutive):
        try:
            if input_x == -1 or input_y == -1:
                raise OutsideOfBoardError
            if num_consecutive == 4:
                return True
            else:
                if self.gameBoard[input_x-1][input_y-1] == self.gameBoard[input_x][input_y]:
                    return self.check_northwest(input_x-1, input_y-1, num_consecutive + 1)
                else:
                    return False
        except IndexError:
            return False

    def check_northeast(self, input_x, input_y, num_consecutive):
        try:
            if input_x == -1 or input_y == -1:
                raise OutsideOfBoardError
            if num_consecutive == 4:
                return True
            else:
                if self.gameBoard[input_x-1][input_y+1] == self.gameBoard[input_x][input_y]:
                    return self.check_northeast(input_x-1, input_y+1, num_consecutive + 1)
                else:
                    return False
        except IndexError:
            return False

    def check_southwest(self, input_x, input_y, num_consecutive):
        try:
            if input_x == -1 or input_y == -1:
                raise OutsideOfBoardError
            if num_consecutive == 4:
                return True
            else:
                if self.gameBoard[input_x+1][input_y-1] == self.gameBoard[input_x][input_y]:
                    return self.check_southwest(input_x+1, input_y-1, num_consecutive + 1)
                else:
                    return False
        except IndexError:
            return False

    def check_southeast(self, input_x, input_y, num_consecutive):
        try:
            if input_x == -1 or input_y == -1:
                raise OutsideOfBoardError
            if num_consecutive == 4:
                return True
            else:
                if self.gameBoard[input_x+1][input_y+1] == self.gameBoard[input_x][input_y]:
                    return self.check_southeast(input_x+1, input_y+1, num_consecutive + 1)
                else:
                    return False
        except IndexError:
            return False
    ###################################################################################

    """Inserts a token at a specific location. Only used for testing."""
    def insert_token(self, input_x, input_y, input_token):
        self.gameBoard[input_x][input_y] = input_token

    """Check for a Connect Four win condition in all eight directions and sets the winner"""
    def win_check(self):
        for i in range(self.row):
            for j in range(self.col):
                try:
                    if self.gameBoard[i][j] != ".":
                        if self.check_north(i, j, 1):
                            self.winner = self.gameBoard[i][j]
                            return True
                        elif self.check_south(i, j, 1):
                            self.winner = self.gameBoard[i][j]
                            return True
                        elif self.check_west(i, j, 1):
                            self.winner = self.gameBoard[i][j]
                            return True
                        elif self.check_east(i, j, 1):
                            self.winner = self.gameBoard[i][j]
                            return True
                        elif self.check_northwest(i, j, 1):
                            self.winner = self.gameBoard[i][j]
                            return True
                        elif self.check_northeast(i, j, 1):
                            self.winner = self.gameBoard[i][j]
                            return True
                        elif self.check_southeast(i, j, 1):
                            self.winner = self.gameBoard[i][j]
                            return True
                        elif self.check_southwest(i, j, 1):
                            self.winner = self.gameBoard[i][j]
                            return True
                        else:
                            continue
                    else:
                        continue
                #If a check is performed outside the bounds of the board, move on to the next token
                except IndexError:
                    continue
                #Check for when input_x or input_y decrements to -1
                except OutsideOfBoardError:
                    continue
        return False

    """Check for a draw"""
    def is_draw(self):
        for i in range(0,self.row):
            for j in range(0, self.col):
                if self.gameBoard[i][j] == ".":
                    return False
        return True

    """Returns a list of valid moves from the current state"""
    def get_valid_moves(self):
        valid_moves = []
        for i in range(0, self.col):
            try:
                tempGameBoard = deepcopy(gameBoardState(self.row, self.col, self.player1, self.gameBoard))
                tempGameBoard.place_token(self.player1, i)
            except InvalidMoveError:
                continue
            valid_moves.append(tempGameBoard)
        return valid_moves


"""Monte Carlo Tree Search"""


class MCTS:
    def __init__(self, inputGameBoard, inputMaxSamples, player1, player2):
        self.player = player1
        self.enemy = player2
        self.current_state = inputGameBoard
        self.max_samples = inputMaxSamples

    """Determines the best move out of all valid moves over rollout of specified time. Refer to document"""
    def get_best_move(self):
        valid_moves = self.current_state.get_valid_moves()
        imaginary_moves = deepcopy(valid_moves)
        current_best_move = valid_moves[0]
        current_best_imaginary = imaginary_moves[0]
        current_best_confidence = 0.0
        sim_count = 0

        """Begin with a single simulation for every move to initialize UCT scores"""
        for move in imaginary_moves:
            self.simulate(move)

        """Simulate the best performing move until starts to underperform"""
        while sim_count < self.max_samples:
            for i in range(0, len(imaginary_moves)):
                current_confidence = self.calculateUpperConfidenceBound(imaginary_moves[i])
                if current_confidence >= current_best_confidence:
                    current_best_confidence = current_confidence
                    current_best_move = valid_moves[i]
                    current_best_imaginary = imaginary_moves[i]
            self.simulate(current_best_imaginary)
            sim_count += 1
        current_best_move.print_board()
        print("Estimated wins: " + str(current_best_imaginary.payout_score))
        print("Probability of winning: " + str(current_best_confidence))
        return current_best_move.gameBoard

    """Play a random game with an imaginary opponent with random moves for both players until terminal state"""
    def simulate(self, inputGameBoard):
        while not inputGameBoard.win_check() or not inputGameBoard.is_draw():
            valid_p1 = False
            valid_p2 = False
            while not valid_p1:
                try:
                    inputGameBoard.place_token(self.player, random.randint(0, inputGameBoard.col-1))
                    valid_p1 = True
                    if inputGameBoard.win_check():
                        inputGameBoard.payout_score += 1
                        inputGameBoard.local_samples += 1
                        return
                    elif inputGameBoard.is_draw():
                        inputGameBoard.payout_score += 0.5
                        inputGameBoard.local_samples += 1
                        return
                except InvalidMoveError:
                    continue
            while not valid_p2:
                try:
                    inputGameBoard.place_token(self.player, random.randint(0, inputGameBoard.col-1))
                    valid_p2 = True
                    if inputGameBoard.win_check():
                        inputGameBoard.local_samples += 1
                        return
                    elif inputGameBoard.is_draw():
                        inputGameBoard.local_samples += 1
                        inputGameBoard.payout_score += 0.5
                        return
                except InvalidMoveError:
                    continue
    """Where the real magic happens"""
    def calculateUpperConfidenceBound(self, inputGameBoard):
        return float((inputGameBoard.payout_score/inputGameBoard.local_samples) + (math.sqrt(2) *
            math.sqrt(math.log(self.max_samples)/inputGameBoard.local_samples)))


"""Initial board"""
initialState = gameBoardState(6, 7, "R")

"""Setup for the game loop"""
player1 = MCTS(initialState, NUM_SIMULATIONS_P1, "R", "Y")
globalBoard = gameBoardState(6, 7, "Y", player1.get_best_move())
player2 = MCTS(globalBoard, NUM_SIMULATIONS_P2, "Y", "R")
globalBoard = gameBoardState(6, 7, "R", player2.get_best_move())

"""Play until victory on either side"""
while (not globalBoard.win_check()) and (not globalBoard.is_draw()):
    player1 = MCTS(globalBoard, NUM_SIMULATIONS_P1, "R", "Y")
    globalBoard = gameBoardState(6, 7, "Y", player1.get_best_move())
    if globalBoard.win_check() or globalBoard.is_draw():
        break
    player2 = MCTS(globalBoard, NUM_SIMULATIONS_P2, "Y", "R")
    globalBoard = gameBoardState(6, 7, "R", player2.get_best_move())

print("The winner is " + globalBoard.winner)