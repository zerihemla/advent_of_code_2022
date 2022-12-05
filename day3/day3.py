from collections import Counter 


def seperate_rucksack(line):
	line_len = len(line)
	seperate_point = int(line_len / 2)
	# print(line_len)
	# print(seperate_point)

	rucksack1 =line[:seperate_point]
	rucksack2 = line[seperate_point:]

	# print(rucksack1)
	# print(rucksack2)

	return rucksack1, rucksack2

def find_common_letter(str1, str2, str3 = None):
	d1 = Counter(str1)
	d2 = Counter(str2)
	common_letter_dict = 0

	if str3 != None:
		d3 = Counter(str3)
		common_letter_dict = d1 & d2 & d3

	else:
		common_letter_dict = d1 & d2

	key = common_letter_dict.keys()
	char_val = "0"
	for i in key:
		char_val = i
	return char_val
	

def find_letter_value(letter_str):
	ret_val = 0

	if letter_str.isupper():
		ret_val = ord(letter_str) -38
		# print (ret_val)

	else:
		ret_val = ord(letter_str) - 96

	# print(letter_str)
	# print(ret_val)

	return ret_val


if __name__ == "__main__":
	input_file = open("day3.txt", "r") 
	lines = input_file.readlines()

	total_value1 = 0
	total_value2 = 0

	elf1 = None
	elf2 = None
	elf3 = None


	#PART1
	for line in lines:
		line = line.strip("\n")

		sack1, sack2 = seperate_rucksack(line)
		common_letter = find_common_letter(sack1, sack2)
		letter_val = find_letter_value(common_letter)
		total_value1 += letter_val

	#PART2
	for line in lines:
		line = line.strip("\n")

		if elf1 == None:
			elf1 = line

		elif elf2 == None:
			elf2 = line

		elif elf3 == None:
			elf3 = line
			common_letter = find_common_letter(elf1, elf2, elf3)
			# print(common_letter)
			letter_val = find_letter_value(common_letter)
			total_value2 += letter_val

			elf1 = None
			elf2 = None
			elf3 = None


	print("TOTAL VALUE1: " + str(total_value1))
	print("TOTAL VALUE2: " + str(total_value2))