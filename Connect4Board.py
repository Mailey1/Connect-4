import copy

class Connect4Board:
	def __init__(self, size):
		self.num_rows = size - 1
		self.num_cols = size
		self.board = [[0 for i in range(self.num_rows)] for j in range(self.num_cols)]
		self.column_capacity = {x : 0 for x in range(size)}
		self.num_turns = 0;
		
	# Copies another instance of a board...
	def copy_board(self, new_board):
		self.num_rows = new_board.num_rows
		self.num_cols = new_board.num_cols
		self.board = copy.deepcopy(new_board.board)
		self.column_capacity = new_board.column_capacity.copy()
		self.num_turns = new_board.num_turns
	
	# Place piece in the column called. The value in column capacity corresponds to the row where the piece will fall when placed in 
	# that column. If that column has a capacity of 7, it is full and the piece cannot be placed there.
	def insert_piece(self, column_number, colour):
		if column_number > self.num_cols - 1:
			return False
		if self.column_capacity[column_number] == self.num_rows:
			return False
		self.board[column_number][self.column_capacity[column_number]] = colour;
		self.column_capacity[column_number] += 1
		self.num_turns += 1
		return True
		
	# iterate across the columns (second index), and print out the entries of the rows from the bottom up.
	def has_winner(self, colour):
		# iterate through each column and check for a win
		for i in range(self.num_cols):
			for j in range(self.num_rows - 3):
				if (colour == self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]):
					return True
		# Now iterate through each row
		for j in range(self.num_rows):
			for i in range(self.num_cols - 3):
				if (colour == self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]):
					return True
		# Now check forward diagonals
		for i in range(self.num_cols - 3):
			for j in range(self.num_rows - 3):
				if (colour == self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]):
					return True
		# Now the back diagonals
		for i in range(self.num_cols - 1, 2, -1):
			for j in range(self.num_rows - 3):
				if (colour == self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2] == self.board[i-3][j+3]):
					return True
		return False
		
	# Assume that the board currently has no connect 4's. Place the computer's coloured piece in every single open (0) cell
	# on the board, then check if the creates a connect 4. Then do the same for the player's coloured pieces, and the heuristic
	# is the difference.
	def eval_board(self, computer_colour, player_colour):
		computer_wins = 0
		player_wins = 0
		# Use a board copy just to be safe.
		board2 = Connect4Board(1)
		board2.copy_board(self)
		
		# Iterate over every entry in board2, if it's empty then it's cell is a 0. If that's the case fill it with a piece
		# of the computer's colour and check if it's a win. Then do the same for the player colour. Then change it back to a 0.
		for i in range(board2.num_cols):
			for j in range(board2.num_rows):
				if board2.board[i][j] != 0:
					continue
				board2.board[i][j] = computer_colour
				if board2.has_winner(computer_colour):
					computer_wins += 1
				board2.board[i][j] = player_colour
				if board2.has_winner(player_colour):
					player_wins += 1
				board2.board[i][j] = 0
				
		return computer_wins - player_wins
		
	# Returns a list containing all valid successors, unless the board already contains a victory.
	# Let turn = 0 denote the computer's turn, 1 denote player turn
	def get_successors(self, computer_colour, player_colour, turn):
		successors = []
		if (self.has_winner(computer_colour) or self.has_winner(player_colour)):
			return successors
		colour = computer_colour
		if turn == 1:
			colour = player_colour
		for i in range(self.num_cols):
			successor = Connect4Board(0)
			successor.copy_board(self)
			if successor.insert_piece(i, colour):
				successors += [successor]
		return successors
		
	def __str__(self):
		output = ""
		space = ""
		for j in range(self.num_rows):
			for i in range(self.num_cols):
				output += str(self.board[i][self.num_rows - 1 - j])
				space = " "
				output += space
			output += '\n'
		return output
		
		
	