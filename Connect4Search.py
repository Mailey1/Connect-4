class Connect4Search:
	def __init__(self, game_board):
		self.game_board = game_board
		
	def best_move(self, depth, computer_colour, player_colour):
		alpha = -10000
		beta = 10000
		best_state = None
		# To start, we get the successors of the computer's moves, so turn = 0 in get_successors call.
		for state in self.game_board.get_successors(computer_colour, player_colour, 0):
			min = self.min_value(state, alpha, beta, depth, computer_colour, player_colour)
			if alpha < min:
				best_state = state
				alpha = min
		return best_state
		
	def min_value(self, board_state, alpha, beta, depth, computer_colour, player_colour):
		if depth == 0:
			return board_state.eval_board(computer_colour, player_colour)
		# In min value, it is simulating the play of the player, so all the successors are possible moves
		# of the player. Therefore turn = 1 in get_successors call.
		successors = board_state.get_successors(computer_colour, player_colour, 1)
		if successors == []:
			return board_state.eval_board(computer_colour, player_colour)
		beta = 10000
		for state in successors:
			beta = min(beta, self.max_value(state, alpha, beta, depth - 1, computer_colour, player_colour))
			if alpha >= beta:
				return beta
		return beta
	
	def max_value(self, board_state, alpha, beta, depth, computer_colour, player_colour):
		if depth == 0:
			return board_state.eval_board(computer_colour, player_colour)
		# In max value, it is simulating the play of the computer, so all the successors are possible moves
		# of the computer. Therefore turn = 0 in get_successors call.
		successors = board_state.get_successors(computer_colour, player_colour, 0)
		if successors == []:
			return board_state.eval_board(computer_colour, player_colour)
		alpha = -10000
		for state in successors:
			alpha = max(alpha, self.min_value(state, alpha, beta, depth - 1, computer_colour, player_colour))
			if alpha >= beta:
				return alpha
		return alpha