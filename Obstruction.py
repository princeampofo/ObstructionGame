import random
import os

#Constants
NUM_PLAYERS=2
NUM_ROWS =6
NUM_COLS =6
PLAYERS_CHECKERS=['X','O']

#Board matrix
Board=[]

#Alphabet matrix
Alpha_matrix = []

#Matrix for alphabets printed on screen
Alpha_output_matrix=[]

#generates a random number to choose the first player
first_turn= random.randint(0,NUM_PLAYERS-1)


def main():
	#This is the main function in which different functions of the game are used.

	play_again = 'Y'

	#game loop if user wants to play again
	while play_again == 'Y':                                             
		print( 'Welcome to Obstruction Game!')

		# calls board function
		board()   

		#calls checker function                                                       
		checker_func()

		print('Would you want to play again? (Y/N) :', end = '')

		#Takes input if user wants to play again(converts input if upper case to lower case)
		play_again = input().upper() 

		#clears board for a new game    
		Board.clear()                                                                           

def board():

	#This function prints the board to the user.

	for alpha in range(65 , 65+26):
		Alpha_matrix.append(chr(alpha))

	for row in range(NUM_ROWS):
		row_list = []
		for col in range(NUM_COLS):
			row_list.append(' ')
		Board.append(row_list)

	print(' ', end ='')
	for alpha in range(NUM_COLS):
		print('   '+Alpha_matrix[alpha],end='')
		Alpha_output_matrix.append(Alpha_matrix[alpha])
	print()
	for r in range(NUM_ROWS):
		print(('  ')+'+---'*NUM_COLS+('+'))
		if len(str(r)) == 2:
			print(str(r)+'|',end='')
		else:
			print(str(r)+' |', end = '')
		for c in range(NUM_COLS):
			print(' '+Board[r][c]+' '+'|',end= '')
		print()
	print(('  ')+'+---'*NUM_COLS+('+'))
	print()

def cell_blocker(row_cord,col_cord):

	#This function blocks neighbouring cells after checker is placed depending on the coordinates.
	
	#top left corner coordinate on the board
	if row_cord == 0 and col_cord == 0:
		for r in range(row_cord,row_cord+2):
			for c in range(col_cord,col_cord+2):
				if Board[r][c] ==" ":
					Board[r][c]= '#'

	#down left corner coordinate on the board
	elif row_cord == NUM_ROWS-1 and col_cord == 0:
		for r in range( NUM_ROWS-2 , NUM_ROWS):
			for c in range(col_cord,col_cord+2):
				if Board[r][c]== " ":
					Board[r][c]='#'

	#top right corner coordinate on the board
	elif row_cord == 0 and col_cord == NUM_COLS -1:
		for r in range(row_cord,row_cord+2):
			for c in range(NUM_COLS-2,NUM_COLS):
				if Board[r][c]== " ":
					Board[r][c]='#'

	#down right corner coordinate on the board
	elif row_cord == NUM_ROWS-1 and col_cord == NUM_COLS-1:
		for r in range (NUM_ROWS-2, NUM_ROWS):
			for c in range(NUM_COLS-2,NUM_COLS):
				if Board[r][c]== " ":
					Board[r][c]='#'

	#coordinates in between top left and down left corner on the board
	elif (0 < row_cord < NUM_ROWS-1) and col_cord==0:
		for r in range(row_cord-1,row_cord+2):
			for c in range(col_cord,col_cord+2):
				if Board[r][c]== " ":
					Board[r][c]='#'

	#coordinates in between top right and down right corner on the board
	elif (0 < row_cord < NUM_ROWS-1) and col_cord==NUM_COLS-1:
		for r in range(row_cord-1,row_cord+2):
			for c in range(NUM_COLS-2,NUM_COLS):
				if Board[r][c]== " ":
					Board[r][c]='#'
	
	#coordinates in between top left and top right corner on the board				
	elif row_cord == 0 and (0 < col_cord < NUM_COLS-1):
		for r in range(row_cord,row_cord+2):
			for c in range(col_cord-1,col_cord+2):
				if Board[r][c]== " ":
					Board[r][c]='#'

	#coordinates in between down left and down right corner on the board
	elif row_cord == NUM_ROWS-1 and (0 < col_cord < NUM_COLS-1):
		for r in range(NUM_COLS-2,NUM_COLS):
			for c in range(col_cord-1,col_cord+2):
				if Board[r][c]== " ":
					Board[r][c]='#'

	#any other coordinates on the board
	else:
		for r in range(row_cord-1,row_cord+2):
			for c in range(col_cord-1,col_cord+2):
				if Board[r][c] == ' ':
					Board[r][c]= '#'

def winner():

	#This function checks for a winner 

	count = 0
	for r in range(NUM_ROWS):
		for c in range(NUM_COLS):
			if Board[r][c] == " ":
				count +=1
	if count == 0:
		return True	

	return False

def checker_func():
	#This function places checkers in the game board,block neighbouring cells and checks for the winner.

	global first_turn                        
	print("You are the first to place your checker ",end ='')
	end_game = False

	#game loop
	while not end_game :
		checker = " "

		#getting user input and validating it
		while not ((len(checker)==2 or len(checker) == 3) and checker[0].isalpha() and checker[0] in Alpha_output_matrix and checker[1:].isdigit() and int(checker[1:]) <NUM_ROWS ):
			print("Player",PLAYERS_CHECKERS[first_turn])
			print("Input your coordinates in this form.eg.A2")
			checker = input("Place your checker :")
			if not ((len(checker)==2 or len(checker) == 3) and checker[0].isalpha() and checker[0] in Alpha_output_matrix and checker[1:].isdigit() and int(checker[1:]) <NUM_ROWS ):
				print("Invalid input!Check your coordinates")

		#placing the checker in the board
		alpha_index = Alpha_output_matrix.index(checker[0])
		digit_index = int(checker[1:])
		if Board[digit_index][alpha_index] == " ":
			Board[digit_index][alpha_index] = PLAYERS_CHECKERS[first_turn]

			#clears screen
			os.system("clear")

			#blocking neigbouring cells
			cell_blocker(digit_index,alpha_index)

			#printing the board
			board()

			#checking for a winner
			end_game = winner()
			if end_game == True:
				print("Congratulations!!! You won Player",PLAYERS_CHECKERS[first_turn])
				print("Better luck next time Player",PLAYERS_CHECKERS[(first_turn+1)%NUM_PLAYERS])
				print()

			#alternating turns between players	
			first_turn=(first_turn+1)%NUM_PLAYERS

		#if cell is already occupied	
		else:
			print("Position occupied!")
		

#main function call
main()