from Connect4Board import Connect4Board
from Connect4Search import Connect4Search

game = Connect4Board(7)
print(game)
search = Connect4Search(game)
human_turn = True
print("Human will play red ('R'), computer will play black ('B')")

while True:
	if human_turn:
		move = int(input("Choose a valid column to place your piece (1-7)\n"))
		x = game.insert_piece(move - 1, 'R')
		if x == False:
			print("Not a valid move, choose a column from 1-7")
			continue
		print(game)
		if game.has_winner('R'):
			print("You won!")
			break
		human_turn = False
	else:
		computer_played = search.best_move(5, 'B', 'R')
		game.copy_board(computer_played)
		print(game)
		print("Computer has (randomly) placed his piece in column " + str(move + 1))
		if game.has_winner('B'):
			print("You lost!")
			break
		human_turn = True