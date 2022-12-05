
cont = True
sum_list = []
rolling_sum = 0

input_file = open("day1.txt", "r") 
lines = input_file.readlines()

for line in lines:
	
	if len(line) < 3:
		sum_list.append(rolling_sum)
		rolling_sum = 0

	else:
		try:
			line_int = int(line)
			rolling_sum += line_int
		except:
			pass

print("Sum List")
print(sum_list)

max_lists = []
for i in range(3):
	temp_max = (max(sum_list))
	max_lists.append(temp_max)
	sum_list.remove(temp_max)

print("Max List:")
print(max_lists)

max_sum = 0
for temp_max in max_lists:
	max_sum += temp_max

print("Total Maxes: " + str(max_sum))