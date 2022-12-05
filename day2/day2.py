OPPONENT_ROCK = "A"
OPPONENT_PAPER = "B"
OPPONENT_SCISORS = "C"

MY_ROCK = "X"
MY_PAPER = "Y"
MY_SCISSORS = "Z"


NEED_TO_LOSE = "X"
NEED_TO_DRAW = "Y"
NEED_TO_WIN = "Z"


ROCK_CONST = "R"
PAPER_CONST = "P"
SCISSORS_CONST = "S"


ROCK_POINT_VALUE = 1
PAPER_POINT_VALUE = 2
SCISSORS_POINT_VALUE = 3


ROUND_WIN_VALUE = 6
ROUND_DRAW_VALUE = 3
ROUND_LOSE_VALUE = 0


def get_win_loss_points(their_move, my_move):

	retVal = ROUND_LOSE_VALUE

	if their_move == my_move:
		retVal = ROUND_DRAW_VALUE

	elif their_move == ROCK_CONST and my_move == PAPER_CONST:
		retVal = ROUND_WIN_VALUE

	elif their_move == PAPER_CONST and my_move == SCISSORS_CONST:
		retVal = ROUND_WIN_VALUE

	elif their_move == SCISSORS_CONST and my_move == ROCK_CONST:
		retVal = ROUND_WIN_VALUE

	return retVal

def need_to_points(need_const):
	retVal = 0

	if NEED_TO_WIN in need_const:
		retVal = ROUND_WIN_VALUE

	elif NEED_TO_DRAW in need_const:
		retVal = ROUND_DRAW_VALUE

	else:
		retVal = ROUND_LOSE_VALUE

	return retVal


def get_throw_points(my_move):
	
	retVal = 0

	if my_move == ROCK_CONST:
		retVal = ROCK_POINT_VALUE

	elif my_move == PAPER_CONST:
		retVal = PAPER_POINT_VALUE

	elif my_move == SCISSORS_CONST:
		retVal = SCISSORS_POINT_VALUE

	return retVal

def convert_to_const(move):
	retVal = "NA"

	if MY_ROCK in move or OPPONENT_ROCK in move:
		retVal = ROCK_CONST

	elif MY_SCISSORS in move or OPPONENT_SCISORS in move:
		retVal = SCISSORS_CONST

	elif MY_PAPER in move or OPPONENT_PAPER in move:
		retVal = PAPER_CONST

	return retVal

def find_my_move(their_move, round_need):
	retVal = "NA"

	if NEED_TO_WIN in round_need:
		
		if their_move == ROCK_CONST:
			retVal = PAPER_CONST

		elif their_move == PAPER_CONST:
			retVal = SCISSORS_CONST

		elif their_move == SCISSORS_CONST:
			retVal = ROCK_CONST


	elif NEED_TO_LOSE in round_need:
		if their_move == ROCK_CONST:
			retVal = SCISSORS_CONST

		elif their_move == PAPER_CONST:
			retVal = ROCK_CONST

		elif their_move == SCISSORS_CONST:
			retVal = PAPER_CONST


	elif NEED_TO_DRAW in round_need:
		retVal = their_move

	return retVal


def part1_calc(space_split):
	their_move = convert_to_const(space_split[0])
	my_move = convert_to_const(space_split[1])

	round_win_points = get_win_loss_points(their_move, my_move)
	throw_points = get_throw_points(my_move)

	round_total_points = round_win_points + throw_points

	return round_total_points

def part2_calc(space_split):
	their_move = convert_to_const(space_split[0])
	round_need = space_split[1]

	my_move = find_my_move(their_move, round_need)

	round_win_points = need_to_points(round_need)
	throw_points = get_throw_points(my_move)
	round_total_points = round_win_points + throw_points

	return round_total_points


input_file = open("day2.txt", "r") 
lines = input_file.readlines()

total_points_part1 = 0
total_points_part2 = 0

for game_round in lines:
	space_split = game_round.split(" ")

	round1_points = part1_calc(space_split)
	total_points_part1 += round1_points

	round2_points = part2_calc(space_split)
	total_points_part2 += round2_points


print("****PART 1 FINAL SCORE: " + str(total_points_part1) + " ********")
print("****PART 2 FINAL SCORE: " + str(total_points_part2) + " ********")