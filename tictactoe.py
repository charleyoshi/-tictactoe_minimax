X = 'X'
O = 'O'



def play(mode):
    board = [' ' for x in range(10)]
    run = True
    if mode == 1:
        computer = aiMoveRandom
        display_message = 'Random'
    elif mode == 2:
        computer = aiMoveHardCode
        display_message = 'Hardcode'
    elif mode == 3:
        computer = minimax
        display_message = 'Minimax'

    else:
        print('something\'s wrong')
        return

    print(f'You are playing with mode {display_message}')
    print('You are O and the computer is X. You can go first.')

    while run:
        printBoard(board)
        if hasWon(board, O):
            print('O won!')
            return
        elif hasWon(board, X):
            print('X won!')
            return
        elif isBoardFull(board):
            print('Tie!')
            return
        else:
            print('player: ' + player(board))
            if player(board) == O:
                # human's turn
                board = humanMove(board)
            elif player(board) == X:
                board = computer(board)



def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')
    print()


def isBoardFull(board):
    return False if board.count(' ') > 1 else True


def hasWon(board, letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or \
           (board[4] == letter and board[5] == letter and board[6] == letter) or \
           (board[7] == letter and board[8] == letter and board[9] == letter) or \
           (board[1] == letter and board[4] == letter and board[7] == letter) or \
           (board[2] == letter and board[5] == letter and board[8] == letter) or \
           (board[3] == letter and board[6] == letter and board[9] == letter) or \
           (board[1] == letter and board[5] == letter and board[9] == letter) or \
           (board[3] == letter and board[5] == letter and board[7] == letter)


def player(board):
    return O if board.count(O) == board.count(X) else X


def humanMove(board):
    run = True
    while run:
        move = input('Where do you want to put your O in? (1-9)')
        try:
            move = int(move)
            if not(0 < move < 10):
                print('Number out of range (1-9)')
            elif isOccupied(board, move):
                print('Position invalid.')
            else:
                run = False
                return insertMove(board, move, O)
        except ValueError:
            print('Integer between 1 to 9')


def isOccupied(board, move):
    return not(board[move] == ' ')


def insertMove(board, move, player):
    board[move] = player
    return board


def aiMoveRandom(board):
    import random
    run = True
    while run:
        move = random.randrange(1, 10)
        if not(isOccupied(board, move)):
            run = False
            return insertMove(board, move, X)


def aiMoveHardCode(board):
    import random
    pile1 = [1, 3, 7, 9]
    random.shuffle(pile1)
    pile2 = [5, 2, 4, 6, 8]
    random.shuffle(pile2)

    for move in pile1:
        if not(isOccupied(board, move)):
            return insertMove(board, move, X)
    for move in pile2:
        if not(isOccupied(board, move)):
            return insertMove(board, move, X)


def terminal(board):
    return isBoardFull(board) or hasWon(board, O) or hasWon(board, X)


def utility(board):
    if hasWon(board, O):
        return -1
    elif hasWon(board, X):
        return 1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None
    else:
        v, move = maxValue(board)
        return insertMove(board, move, X)


def maxValue(board):
    if terminal(board):
        return utility(board), None
    else:
        v = float('-inf')
        for action in actions(board):
            x, dummy = minValue(result(board, action, X))
            if x > v:
                v = x
                move = action
        return v, move


def minValue(board):
    if terminal(board):
        return utility(board), None
    else:
        v = float('inf')
        for action in actions(board):
            x, dummy = maxValue(result(board, action, O))
            if x < v:
                v = x
                move = action
        return v, move


def actions(board):
    """Return set of possible moves"""
    moves = set()
    for i in range(1, 10):
        if not(isOccupied(board, i)):
            moves.add(i)
    return moves


def result(board, move, player):
    import copy
    board_copy = copy.deepcopy(board)
    new_board = insertMove(board_copy, move, player)
    return new_board



