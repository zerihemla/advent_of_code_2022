def setup_containers(container_list):
	empty_container = []

	container_list.append(empty_container)
	
	container_list.append(["B", "Q", "C"])
	container_list.append(["R", "Q", "W", "Z"])
	container_list.append(["B", "M", "R", "L", "V"])
	container_list.append(["C", "Z", "H", "V", "T", "W"])
	container_list.append(["D", "Z", "H", "B", "N", "V", "G"])
	container_list.append(["H", "N", "P", "C", "J", "F", "V", "Q"])
	container_list.append(["D", "G", "T", "R", "W", "Z", "S"])
	container_list.append(["C", "G", "M", "N", "B", "W", "Z", "P"])
	container_list.append(["N", "J", "B", "M", "W", "Q", "F", "P"])

	# print(container_list)

#This was for part1
# def manipulate_containters(cont_list, num_move, num_from, num_to):
# 	for i in range(num_move):
# 		temp_str = container_list[num_from].pop()
# 		container_list[num_to].append(temp_str)

#This is for part2
def manipulate_containters(cont_list, num_move, num_from, num_to):
	temp_list = []
	temp_str = ""
	for i in range(num_move):
		temp_str = container_list[num_from].pop()
		temp_list.append(temp_str)

	for i in range(num_move):
		temp_str = temp_list.pop()
		container_list[num_to].append(temp_str)



if __name__ == "__main__":
	input_file = open("day5.txt", "r") 
	# input_file = open("day5_short.txt", "r") 
	lines = input_file.readlines()

	elves_work_strings = []
	num_full_contains = 0
	num_partial_contains = 0

	container_list = []

	setup_containers(container_list)

	for line in lines:
		line = line.strip("\n")

		instruction_list = line.split(" ")
		num_move = int(instruction_list[1])
		num_from = int(instruction_list[3])
		num_to = int(instruction_list[5])

		manipulate_containters(container_list, num_move, num_from, num_to)


	ans_string = ""
	for this_list in container_list:
		try:
			temp_str = this_list.pop()
			ans_string += temp_str
			this_list.append(temp_str)
		except:
			pass

	print(ans_string)