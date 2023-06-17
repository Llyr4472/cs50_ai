from tictactoe import *

def test_tic():
    assert tictactoe.terminal([[x, O, X],
                               [O, X, X],
                              [O, X, O]]) == True 