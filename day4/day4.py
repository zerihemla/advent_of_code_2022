def document_work(work_start, work_end):
	total_work_list = []
	for i in range (work_start, work_end+1):
		total_work_list.append(i)

	return total_work_list



# def find_containing(work_string1, work_string2):
	
# 	if (work_string1 in work_string2) or (work_string2 in work_string1):
# 		print(work_string1)
# 		print(work_string2)
# 		print()
# 		return 1


# 	return 0

def get_start_and_end(work_section):
	work_range = work_section.split("-")
	work_start = int(work_range[0])
	work_end = int(work_range[1])
	return work_start, work_end

	

def find_containing(work_start1, work_end1, work_start2, work_end2):
	
	if (work_start1 >= work_start2) and (work_end1 <= work_end2):
		return 1

	elif (work_start2 >= work_start1) and (work_end2 <= work_end1):
		return 1

	return 0

def find_partial_contains(work_start1, work_end1, work_start2, work_end2):
	
	work_list1 = document_work(work_start1, work_end1)
	work_list2 = document_work(work_start2, work_end2)

	for work1 in work_list1:
		for work2 in work_list2:
			if work1 == work2:
				return 1
	return 0


if __name__ == "__main__":
	input_file = open("day4.txt", "r") 
	# input_file = open("day4_short.txt", "r") 
	lines = input_file.readlines()

	elves_work_strings = []
	num_full_contains = 0
	num_partial_contains = 0

	#PART1
	for line in lines:
		line = line.strip("\n")

		work_sections = line.split(",")

		# work_string1 = document_work(work_sections[0])
		# work_string2 = document_work(work_sections[1])

		# num_repeats += find_containing(work_string1, work_string2)
		work_section1_start, work_section1_end = get_start_and_end(work_sections[0])
		work_section2_start, work_section2_end = get_start_and_end(work_sections[1])

		num_full_contains += find_containing(work_section1_start, work_section1_end,
											 work_section2_start, work_section2_end)

		num_partial_contains += find_partial_contains(work_section1_start, work_section1_end,
													  work_section2_start, work_section2_end)


	print("NUM FULL CONTAINS: " +str(num_full_contains))
	print("NUM PARTIAL CONTAINS: " + str(num_partial_contains))

