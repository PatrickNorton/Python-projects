def start():
    board = ['-' for x in range(9)]
    game = True
    ifbot = input('1 or 2 players? ')
    bot = True if ifbot == '1' else False
    while game:
        game = gameplay(board, bot)


def gameplay(board, bot):
    for turn in ['O', 'X']:  # Do something for bot
        validinput = False
        while not validinput:
            print('\n'.join(' '.join(str(z)
                                     for z in board[3*x:3*x+3]) for x in range(3)))
            space = input(
                turn+"'s turn\nWhere do you want to play?\nSpaces are 1-9 ") if not bot or turn != 'X' else thebot(board)
            try:
                playloc = int(space)-1
                (board[playloc], validinput) = (
                    turn, True) if board[playloc] == '-' else ('-', False)
            except TypeError:
                print('Invalid entry! Please try again')
        game = False if wincheck(board, turn) else True
        if wincheck(board, turn):
            game = False
            print(turn+' wins!')
            print('\n'.join(' '.join(str(z)
                                     for z in board[3*x:3*x+3]) for x in range(3)))
            break
        if '-' not in board:
            game = False
            print('\n'.join(' '.join(str(z)
                                     for z in board[3*x:3*x+3]) for x in range(3)))
            print('Tie!')
            break
    return game


def wincheck(board, turn):
    win = False
    for x in range(4):
        if board[4] == board[x] == board[8-x] == turn:
            win = True
            break
    else:
        for x in range(4):
            wincom = [[0, 1, 2], [0, 3, 6], [2, 5, 8], [6, 7, 8]][x]
            if all(board[x] == board[wincom[0]] == turn for x in wincom):
                win = True
                break
    return win


def thebot(board):
    print("Bot's turn")
    testboard = board[:]
    import itertools
    import time
    for x, y in itertools.product(range(9), ['X', 'O']):
        testboard[x] = y if testboard[x] == '-' else testboard[x]
        if wincheck(testboard, y):
            move = x
            break
        testboard = board[:]
    else:
        for x in [0, 2, 6, 8]:
            if board[x] == '-' and board[8-x] == 'O':
                move = x
                break
        else:
            for x in [4, 0, 8, 2, 6, 1, 7, 3, 5]:
                if board[x] == '-':
                    move = x
                    break
    time.sleep(1)
    return move+1


start()
