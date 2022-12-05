ROCK_VAL = 1
PAPER_VAL = 2
SCISORS_VAL = 3

WIN_VAL = 6
LOSE_VAL = 0
DRAW_VAL = 3

part1_dict = {
	"A X": DRAW_VAL + ROCK_VAL,
	"A Y": WIN_VAL	+ PAPER_VAL,
	"A Z": LOSE_VAL	+ SCISORS_VAL,
	"B X": LOSE_VAL	+ ROCK_VAL,
	"B Y": DRAW_VAL	+ PAPER_VAL,
	"B Z": WIN_VAL	+ SCISORS_VAL,
	"C X": WIN_VAL	+ ROCK_VAL,
	"C Y": LOSE_VAL	+ PAPER_VAL,
	"C Z": DRAW_VAL	+ SCISORS_VAL,
}

part2_dict = {
	"A X": LOSE_VAL + SCISORS_VAL,
	"A Y": DRAW_VAL + ROCK_VAL,
	"A Z": WIN_VAL  + PAPER_VAL,
	"B X": LOSE_VAL + ROCK_VAL,
	"B Y": DRAW_VAL + PAPER_VAL,
	"B Z": WIN_VAL  + SCISORS_VAL,
	"C X": LOSE_VAL + PAPER_VAL,
	"C Y": DRAW_VAL + SCISORS_VAL,
	"C Z": WIN_VAL  + ROCK_VAL, 
}

input_file = open("day2.txt", "r") 
lines = input_file.readlines()

total_points_part1 = 0
total_points_part2 = 0

for game_round in lines:
	game_round = game_round.strip("\n")

	part1_round_points = part1_dict[game_round]
	part2_round_points = part2_dict[game_round]

	total_points_part1 += part1_round_points
	total_points_part2 += part2_round_points

print("****PART 1 FINAL SCORE: " + str(total_points_part1) + " ********")
print("****PART 2 FINAL SCORE: " + str(total_points_part2) + " ********")