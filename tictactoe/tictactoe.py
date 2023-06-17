"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0 
    for row in board:
        for column in row:
            if column is not None:
                if column == X: x += 1
                if column == O: o +=1
    if x == o: return X
    else: return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []
    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                moves.append((row,column))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_ = copy.deepcopy(board)
    i,j = action
    board_[i][j] = player(board)
    return board_


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2]: return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2]: return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2]: return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0]: return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]: return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2]: return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2]: return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]: return board[0][2]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for i in board:
        for j in i:
            if j is EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is X:
        return 1
    elif winner(board) is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """ 
    Max = -5
    Min = 5 

    if player(board) is X:
        return maxvalue(board,Max,Min)[0]
    elif player(board) is O:
        return minvalue(board,Max,Min)[0]


def maxvalue(board,Max,Min):
    if terminal(board):
        return None,utility(board)

    move = None
    v = float("-inf")
    for action in actions(board):
        test = minvalue(result(board,action),Max,Min)[1]
        if test > v:
            v = test 
            move = action
        Max = max(Max,test)
        if Min <= Max:
            break
    return move, v


def minvalue(board,Max,Min):
    if terminal(board):
        return None,utility(board)

    move = None
    v = float("inf")
    for action in actions(board):
        test = maxvalue(result(board,action),Max,Min)[1]
        if test < v:
            v= test
            move = action
        Min = min(Min,test)
        if Max >=Min:
            break
    return move,v