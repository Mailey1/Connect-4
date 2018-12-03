class Connect4Board:
	def __init__(self, size):
		self.num_rows = size - 1
		self.num_cols = size
		self.board = [[0 for i in range(self.num_rows)] for j in range(self.num_cols)]
		self.column_capacity = {x : 0 for x in range(size)}
		self.num_turns = 0;
		
		
	# Place piece in the column called. The value in column capacity corresponds to the row where the piece will fall when placed in 
	# that column. If that column has a capacity of 7, it is full and the piece cannot be placed there.
	def insert_piece(self, column_number, colour):
		if column_number > self.num_cols - 1:
			return False
		if self.column_capacity[column_number] == self.num_rows:
			return False
		self.board[column_number][self.column_capacity[column_number]] = colour;
		self.column_capacity[column_number] += 1
		return True
		
		
	# iterate across the columns (second index), and print out the entries of the rows from the bottom up.
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
		
	def has_winner(self, colour):
		# iterate through each column and check for a win
		for i in range(self.num_cols):
			for j in range(self.num_rows - 3):
				if (colour == self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]):
					return "A player has won"
		# Now iterate through each row
		for j in range(self.num_rows):
			for i in range(self.num_cols - 3):
				if (colour == self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]):
					return "A player has won"
		# Now check forward diagonals
		for i in range(self.num_cols - 3):
			for j in range(self.num_rows - 3):
				if (colour == self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]):
					return "A player has won"
		# Now the back diagonals
		for i in range(self.num_cols - 1, 2, -1):
			for j in range(self.num_rows - 1, 2, -1):
				if (colour == self.board[i][j] == self.board[i-1][j-1] == self.board[i-2][j-2] == self.board[i-3][j-3]):
					return "A player has won"
		return "Nobody has won"
		
	