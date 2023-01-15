
board = {1 : ' ', 2 : ' ', 3 : ' ',
		 4 : ' ', 5 : ' ', 6 : ' ',
		 7 : ' ', 8 : ' ', 9 : ' '}

def PrintBoard(board):

	print('')
	print('  ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + '  ')
	print(' ---|---|--- ')
	print('  ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + '  ')
	print(' ---|---|--- ')
	print('  ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + '  ')
	print('')

def CheckForDraw():
	for key in board.keys():
		if board[key] == ' ':
			return False

	return True

def CheckForWin(letter):
	if(board[1] == board[2] and board[1] == board[3] and board[1] == letter):
		return True
	elif(board[4] == board[5] and board[4] == board[6] and board[4] == letter):
		return True
	elif(board[7] == board[8] and board[7] == board[9] and board[7] == letter):
		return True

	elif(board[1] == board[4] and board[1] == board[7] and board[1] == letter):
		return True
	elif(board[2] == board[5] and board[2] == board[8] and board[2] == letter):
		return True
	elif(board[3] == board[6] and board[3] == board[9] and board[3] == letter):
		return True

	elif(board[1] == board[5] and board[1] == board[9] and board[1] == letter):
		return True
	elif(board[3] == board[5] and board[3] == board[7] and board[3] == letter):
		return True

	else:
		return False

def InsertLetter(letter,position):

	if(board[position] == ' '):
		board[position] = letter
		PrintBoard(board)
		if(CheckForDraw()):
			print("It's a draw!!")
			print("Thankyou for playing :)")
			exit()
		if(CheckForWin(letter)):
			print("Bot Wins!!!")
			print("Thankyou for playing :)")
			exit()

	else:
		print("\nPosition already taken!")
		position = int(input("Please enter a valid position: "))
		InsertLetter(letter,position)
		return

def PlayerMove():
	position = int(input("\nYour turn!\nPlease select a position: "))
	InsertLetter(player,position)
	return

def BotMove():
	print("Bot's turn!\nBot plays\n")
	MaxScore = -10
	BestMove = 0

	for key in board.keys():
		if(board[key] == ' '):
			board[key] = bot
			score = MiniMax(board,False)
			board[key] = ' '
			if(score > MaxScore):
				MaxScore = score
				BestMove = key

	InsertLetter(bot,BestMove)
	return

def MiniMax(board,isMaximizing):

	if CheckForWin(bot):
		return 1
	elif CheckForWin(player):
		return -1
	elif CheckForDraw():
		return 0

	if isMaximizing:

		MaxScore = -10

		for key in board.keys():
			if(board[key] == ' '):
				board[key] = bot
				score = MiniMax(board,False)
				board[key] = ' '
				if(score > MaxScore):
					MaxScore = score

		return MaxScore

	else:

		MinScore = 10

		for key in board.keys():
			if(board[key] == ' '):
				board[key] = player
				score = MiniMax(board, True)
				board[key] = ' '
				if(score < MinScore):
					MinScore = score

		return MinScore

print("\n\n------------------------")
print(" IMPOSSIBLE TIC TAC TOE ")
print("------------------------")

PrintBoard(board)

player = 'O'
bot = 'X'

while True:
	BotMove()
	PlayerMove()


