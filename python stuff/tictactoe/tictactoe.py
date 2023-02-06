"""
Tic Tac Toe Player
"""

import math
import copy 
X = "X"
O = "O"
EMPTY = None
memo = {}

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
    CountOfX = 0
    CountOfO = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                CountOfX += 1
            if board[i][j] == O:
                CountOfO += 1

    return X if CountOfX <= CountOfO else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    Actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                Actions.append((i, j))

    return Actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception('Invalid action!')

    NewBoard = copy.deepcopy(board)
    NewBoard[action[0]][action[1]] = player(board)
    return NewBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY: #fuck python
            return board[i][0]

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #return True if winner(board) != None or len(actions(board)) == 0 else False
    if winner(board) != None:
        return True
    for row in board:
        for cell in row:
            if cell == None:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    thewinner = winner(board)
    return 1 if thewinner == X else -1 if thewinner == O else 0

def gethash(board):
    hash = 0
    cnt = 0
    for i in range(3):
        for j in range(3):
            hash += pow(3, cnt) * (0 if board[i][j] == None else 1 if board[i][j] == X else 2)
            cnt += 1
    return str(hash)
'''
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def maximize(board):
        if terminal(board):
            return [utility(board), None]
        all_actions = actions(board)
        best_action = None
        mx = -1000
        for i in all_actions:
            new_board = result(board, i)
            value = minimize(new_board)
            if value[0] > mx:
                mx = value[0]
                best_action = i
                if value[0] == 1:
                    return [value[0], i]
        return [mx, best_action]
    
    def minimize(board):
        if terminal(board):
            return [utility(board), None]
        all_actions = actions(board)
        best_action = None
        mn = 1000
        for i in all_actions:
            new_board = result(board, i)
            value = maximize(new_board)
            if value[0] < mn:
                mn = value[0]
                best_action = i
                if value[0] == -1:
                    return [value[0], i]
        return [mn, best_action]

    if(terminal(board)):
        return None

    curplayer = player(board)
    if(curplayer == 'X'):
        return maximize(board)[1]
    else:
        return minimize(board)[1]
'''
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    hash = gethash(board)
    if(memo.get(hash) != None):
        return memo[hash]

    if terminal(board):
        return None


    curplayer = player(board)
    best_action = None
    best_value = -1 # 1 win 0 draw -1 lose
    possible_actions = actions(board)
    for i in possible_actions:
        
        new_board = result(board, i)
        while not terminal(new_board):
            new_board = result(new_board, minimax(new_board))
            
        winorlose = utility(new_board)

        if not terminal(new_board):
            raise Exception("infinate =========================================D")
        if winorlose == 1 and curplayer == X or winorlose == -1 and curplayer == O:
            best_action = i
            best_value = 1
        elif winorlose == 0:
            if best_value < 1:
                best_value = 0
                best_action = i
        elif best_action == None:
            best_action = i
    memo[hash] = best_action
    return best_action

