from Shogiclasses import piece, coord, board, turntype, captlist, a, b, turn, promoter
from numpy import sin, cos, pi, sign
from itertools import product
from copy import deepcopy
import os, sys
cpath = sys.path[0]

def iterrun(x): return [round(sin(pi*x/4)), -round(cos(pi*x/4))]


def inp2loc(x): return coord(b.index(x[1]), a.index(x[0]))


def playgame():
    """The base layer for the game; changes turn and prints most outputs"""
    global turn
    game, color, turnint = True, ['White', 'Black'], int(turn)
    with open(os.path.join(cpath, 'shogierrors.txt')) as etxt:
        errorlist = [x.strip() for x in etxt]
    while game:
        print(
            f"Black pieces: {' '.join(captlist[1])}\n{board}\nWhite pieces: {' '.join(captlist[0])}")
        print(f"{color[turnint]}'s turn")
        game = piececheck()
        check, kingpos, checklist = checkcheck()
        if check and game:
            mate = matecheck(kingpos, checklist)
            game = not mate
            print(
                f"{board}\nCheckmate! {color[turnint]} wins\n" if mate else 'Check\n')
        turn = turntype(1-int(turn))
        turnint = int(turn)


def piececheck():
    """Asks and validates current location of the piece"""
    global board, error
    game, quitting, error = True, False, 1
    while error:
        pieceloc = input(
            'What is the location of the piece you would like to move? ')
        if inputpiece(pieceloc, quitting):
            if board[inp2loc(pieceloc)].color == str(turn):
                quitting = movecheck(inp2loc(pieceloc))
            print(errorlist[error])
    return not quitting and game


def movecheck(current):
    """Asks and validates the location of where the piece is to be moved"""
    global board
    test, quitting = (False,)*2
    while not test:
        moveloc = input('Where do you want to move this piece? ')
        if inputpiece(moveloc, quitting):
            test = True
            promote, board = movecheck2(current, inp2loc(moveloc))
            if promote and input('Would you like to promote this piece? ').lower().startswith('y'):
                board[inp2loc(moveloc)].promote()
    return quitting


def movecheck2(current, new):
    """Checks whether the piece can be moved to the specified location"""
    move = new-current
    theboard = deepcopy(board)
    piece = theboard[current]
    global captlist, error
    error = 0
    movedir = [iterrun(x) for x in range(8)].index(
        [[1, -1][int(turn)]*sign(x) for x in move]) if any(move) else 8
    magicvar = piece.moves[movedir]
    if not any(move):
        error = 3
    elif board[new].color == str(turn):
        error = 4
    elif magicvar == 'T' and [abs(x) for x in move] == [1, 2]:
        error = 0
    elif not all(move) or abs(move.x) == abs(move.y):
        if magicvar == '+' or (magicvar == '1' and all(abs(x) < 2 for x in move)):
            obscheck(current, new, move)
        else:
            error = 1
    else:
        error = 2
    if not error:
        theboard.move(current, new)
    return promoter(theboard, new) and not error, theboard


def obscheck(current, new, move):
    """Checks whether or not the piece's path is clear"""
    global error
    for x in range(1, abs(move.x if move.x else move.y)):
        error = 2 if not board[current +
                               coord(*[sign(z)*x for z in move])] else error


def checkcheck():
    """Tests to see if the opposition king is in check"""
    global board
    check, checklist = False, []
    oldboard = deepcopy(board)
    kingpos = [coord(x, y) for x, y in board.it()
               if board[x, y] == piece('k', turn.other)][0]
    for x, y in board.it():
        if board[x, y].color == str(turn) and movecheck2(coord(x, y), kingpos)[0]:
            check = True
            checklist.append(coord(x, y))
            if len(checklist) == 2:
                break
        board = deepcopy(oldboard)
    return check, kingpos, checklist


def matecheck(kingpos, checklist):
    """Tests to see if the opposition king is in checkmate"""
    global board
    oldboard = deepcopy(board)
    kingmovepos = [coord(*iterrun(x)) for x in range(8)]
    for kmpiter in kingmovepos:
        if tuple(kingpos+kmpiter) in board.it():
            movecheck2(kingpos, kingpos+kmpiter)
            board = oldboard
            if not error and not checkcheck()[0]:
                return False
    if len(checklist) == 1:
        checklist = checklist[0]
        if captlist[int(turn)] and board[checklist].ptype != 'n' and not all(x in (-1, 0, 1) for x in (checklist-kingpos)):
            return False
        for x, y in board.it():
            if board[x, y].color != turn.other and movecheck2(coord(x, y), checklist)[0]:
                board = oldboard
                return False
        move = kingpos-checklist
        movedir = coord(*[[1, -1][int(turn)]*int(sign(x)) for x in move])
        for (x, y), z in product(board.it(), range(abs(move.x if move.x else move.y))):
            if board[x, y].color != turn.other and movecheck2(coord(x, y), coord(*[z*k for k in checklist*movedir]))[0]:
                board = oldboard
                return False
    return True


def otherconditions(var, quitting):
    """Checks for special conditions in user inputs"""
    if var == 'captured':
        piecemoved = input(
            'Which piece would you like moved? (print the type, no color) ')
        if len(piecemoved) == 1 and piece(piecemoved, str(turn)) in captlist['wb'.index(str(turn))]:
            moveto = input('Where would you like to put this piece? ')
            if inputpiece(moveto, True):
                board.pieces[inp2loc(moveto)] = piece(piecemoved, str(turn))
                captlist.remove(piece(piecemoved, str(turn)))
        else:
            print('Invalid entry! Please try again!')


def inputpiece(var, quitting):
    """Checks to ensure that the entered piece is valid"""
    if len(var) == 2 and var[0] in a and var[1] in b:
        return True
    elif quitting and not otherconditions(var, quitting):
        print('Invalid entry. Please try again.')
        return False


playgame()
