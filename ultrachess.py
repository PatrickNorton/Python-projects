def otherconditions(var,quitting):
	if var == 'help':
		print(open('chesshelp.txt').read());return True
	elif var == 'quit':
		quitting = True if input('Are you sure you want to quit? Retype quit to quit') == 'quit' else False;return True
	return False
def boardpos(x,y):
	return ('abcdefgh'[x]+'87654321'[y])
def matecheck(board,turn,piecedict,kingpos,checklist):
	kingmovepos = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]];import copy,numpy as np,itertools;kingposnew = boardpos(kingpos[0],kingpos[1])
	for z in range(8):
		if 0 <= kingpos[0]+kingmovepos[z][0] <= 7 and 0 <= kingpos[1]+kingmovepos[z][1] <= 7:
			movepos = boardpos(kingpos[0]+kingmovepos[z][0],kingpos[1]+kingmovepos[z][1]);move,_,_ = movecheck2(kingposnew,copy.deepcopy(board),piecedict,turn,movepos,False)
			if not (checkcheck(board,turn,piecedict)[0] if move else True):
				return False
	if len(checklist) == 1:
		checklist = checklist[0]
		for x,y in itertools.product(range(8),range(8)):
			if board[y][x][1] not in [turn,'-'] and movecheck2(boardpos(x,y),copy.deepcopy(board),piecedict,turn,boardpos(checklist[0],checklist[1]),False)[0]:
				return False
		if board[checklist[1]][checklist[0]][0] != 'n':
			movex = kingpos[0]-checklist[0];movey = checklist[1]-kingpos[1];movedir = [('b w'.index(turn)-1)*x for x in [int(np.sign(movex)),-int(np.sign(movey))]]
			for x,y,z in itertools.product(range(8),range(8),range(abs(movex) if movex else abs(movey))):
				if board[y][x][1] not in [turn,'-'] and movecheck2(boardpos(x,y),copy.deepcopy(board),piecedict,turn,boardpos(checklist[0]*movedir[0]*z,checklist[1]*movedir[1]*z),False)[1]:
					return False
	return True
def checkcheck(board,turn,piecedict):
	import itertools,copy;check,checklist = False,[]
	kingpos = [[x,y,board[y][x]] for x,y in itertools.product(range(8),range(8)) if board[y][x][0] == 'k']
	kingpos = kingpos[0 if kingpos[0][2][1] != turn else 1]
	for x,y in itertools.product(range(8),range(8)):
		if movecheck2(boardpos(x,y),copy.deepcopy(board),piecedict,turn,boardpos(kingpos[0],kingpos[1]),False)[0] if board[y][x][1] == turn else False:
			check = True;checklist.append([y,x])
			if len(checklist) > 1:
				break
	return check,kingpos,checklist
def obscheck(currentx,currenty,board,movex,movey,turn):
	import numpy as np;move,error = True,0
	for x in range(1,abs(movex if movex else movey)):
		move,error = (False,4) if board[currenty+int(np.sign(movey))*x][currentx+int(np.sign(movex))*x] != '--' else (move,error)
	move,error = (False,5) if board[currenty+movey][currentx+movex][1] == turn else (move,error)
	return move,error
def movecheck(pieceloc,board,piecedict,turn,enpassant):
	test,move,error,test2 = False,0,0,False
	while not test:
		moveloc = input('Where do you wish to move this piece? ')
		if moveloc[0] in 'abcdefgh' and moveloc[1] in '87654321' and len(moveloc) == 2:
			test = True;quitting = False;move,error,pawnchange = movecheck2(pieceloc,board,piecedict,turn,moveloc,enpassant)
			while test2 if move and pawnchange else False:
				newpiece = input('What would you like this piece to become? ')
				(board['abcdefgh'.index(moveloc[0])]['87654321'.index(moveloc[1])],test2) = (newpiece+turn,True) if newpiece in 'pnbrq' else (None,False)
				print('Success!' if test2 else 'Error')
		elif not otherconditions(moveloc,quitting):
			print('Invalid entry! Please try again.')
	return move,error,quitting
def movecheck2(pieceloc,board,piecedict,turn,moveloc,enpassant):
	a,b = 'abcdefgh','87654321';import numpy as np;error = 0;currentx = a.find(pieceloc[0]);currenty = b.find(pieceloc[1]);movex = (a.find(moveloc[0])-currentx);movey = (b.find(moveloc[1])-currenty)
	a = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,0]];movedir = a.index([int(np.sign(movex)),-int(np.sign(movey))]) if turn == 'w' else a.index([-int(np.sign(movex)),int(np.sign(movey))])
	piece = board[currenty][currentx];magicvar = piecedict[[x[0] for x in piecedict].index(piece[0])][2][movedir];pawnchange = False;obsvars = (currentx,currenty,board,movex,movey,turn)
	if piece[0] == 'n':
		move,error = (True,0) if (abs(movex) == 2 and abs(movey) == 1) or (abs(movey) == 2 and abs(movex) == 1) and piece[1] != turn else (False,1)
	elif piece[0] == 'p':
		if abs(movex) == abs(movey) == 1 and magicvar == '*' and (board[currenty+movey][currentx+movex][1] not in [turn,'-'] or enpassant is not None):
			move = True if enpassant is None else (True if enpassant[0] == currentx+movex and enpassant[1] == currenty+movey else False)
		elif abs(movey) in [1,2] and magicvar == '1' and board[currenty+movey][currentx] == '--':
			move,error = (True,0) if abs(movey) == 1 else (obscheck(*obsvars) if abs(movey) == 2 and currenty == [6,1][['w','b'].index(piece[1])] else (move,error))
			enpassant = (currentx+movex,currenty+movey+(-1 if turn == 'b' else 1)) if abs(movey) == 2 and currenty == [6,1][['w','b'].index(piece[1])] else None
		else:
			move = False;error = 1
		pawnchange = True if currenty+movey in [0,7] and move else False
	elif not movex and not movey:
		move = False;error = 1
	elif (not movex or not movey or abs(movex) == abs(movey)) and (movex or movey):
		move,error = obscheck(*obsvars) if magicvar == '+' or (magicvar == '1' and abs(movex),abs(movey) < 2,2) else (False,2)
	else:
		move = False;error = 2
	if move:
		board[currenty+movey][currentx+movex] = piece;board[currenty][currentx] = '--'
	return move,error,pawnchange
def piececheck(board,piecedict,turn):
	test,move,game,quitting,enpassant = False,False,True,False,False
	while not test or not move:
		pieceloc = input('What is the location of the piece you wish to move? ')
		if len(pieceloc) == 2 and (pieceloc[0] in 'abcdefgh' and pieceloc[1] in '87654321'):
			if board['87654321'.find(pieceloc[1])]['abcdefgh'.find(pieceloc[0])][1] == turn:
				test = True;move,error,quitting = movecheck(pieceloc,board,piecedict,turn,enpassant)
				print(open('Chesserrors.txt').readlines()[error])
			else:
				print('That space does not have one of your pieces!')
		elif not otherconditions(pieceloc,quitting):
			print('Invalid entry! Please try again.')
		game = False if quitting else game
	return game
def playgame(board,piecedict):
	game,person,color = True,['w','b'],['White','Black']
	while game:
		for which in range(2):
			print('\n'.join('87654321'[x]+' '+' '.join(str(y) for y in board[x]) for x in range(8)),'\n  '+'  '.join(str(y) for y in 'abcdefgh'))
			turn = person[which];print(f"{color[which]}'s turn")
			game = piececheck(board,piecedict,turn);check,kingpos,checklist = checkcheck(board,turn,piecedict)
			if check and game:
				mate = matecheck(board,turn,piecedict,kingpos,checklist);game = False if mate else True
				print('\n'.join('87654321'[x]+' '+' '.join(str(y) for y in board[x]) for x in range(8)),'\n  '+'  '.join(str(y) for y in 'abcdefgh'))
				print(f'Checkmate! {color[which]} wins\n' if mate else 'Check\n')
def createboard():
	board = [['--' for x in range(8)] for y in range(8)]
	piecedict = [i.strip().split(',') for i in open('chesspieces.txt').readlines()]
	board[0] = ['rb','nb','bb','qb','kb','bb','nb','rb'];board[1] = ['pb' for x in range(8)];board[6] = ['pw' for x in range(8)];board[7] = ['rw','nw','bw','qw','kw','bw','nw','rw']
	#T means knight's move, 2 fwd. 1 to L/R
	#+ means ranging move, inf. distance in that dir.
	playgame(board,piecedict)
createboard()