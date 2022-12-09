TOTAL_DISK_SPACE = 70000000
UPDATE_SIZE = 30000000

class CustomFile:
	def __init__(self, name, size):
		self.name = name
		self.size = size

	def print(self):
		print(self.name + ": " + str(self.size))


class CustomTree:
	def __init__(self, name, parent = None):
		self.parent = parent
		self.name = name
		self.fileList = []
		self.directoryList = []
		self.total_size = 0
		self.processed = False
		self.is_init = False

	def return_dir_by_name(self, dir_name):
		ret_val = self
		for dir in self.directoryList:
			if dir.name == dir_name:
				ret_val = dir
				break
		else:
			print("ERROR!!! DID NOT FIND DIRECTORY WITH NAME! " + dir_name)

		return ret_val

	def print_all(self):
		print("Current Dir: " + self.name)
		print("-----")
		self.print_file_list()
		print("-----")
		self.print_directory_list()
		print("-----")
		self.print_parent()
		print("*****\n*****")

		for directory in self.directoryList:
			directory.print_all()

	def print_name(self):
		print("Dir Name: " + self.name)

	def print_file_list(self):
		if len(self.fileList) > 0:
			print("Files List:")
			for file in self.fileList:
				file.print()
		else:
			print("NO FILES!")

	def print_directory_list(self):
		if len(self.directoryList) > 0:
			print("Dir List:")
			for directory in self.directoryList:
				directory.print_name()
		else:
			print("NO DIRECTORIES!")

	def print_parent(self):
		if self.parent == None:
			print("NO PARENT!")
		else:
			print("Parent is: ")
			self.parent.print_name()

	def process_sizes(self):
		directory_sizes = 0
		file_sizes = 0
		if len(self.directoryList) > 0:
			for dir in self.directoryList:
				dir.process_sizes()
				directory_sizes += dir.total_size

		if len(self.fileList) > 0:
			for file in self.fileList:
				file_sizes += file.size

		self.total_size = directory_sizes + file_sizes
		self.processed = True

	def find_min_sizes(self, min_size):
		if len(self.directoryList) > 0:
			for dir in self.directoryList:
				dir.find_min_sizes(min_size)

		if self.total_size <= min_size:
			print(str(self.total_size))

	def find_size_range(self, min_size, max_size):
		if len(self.directoryList) > 0:
			for dir in self.directoryList:
				dir.find_size_range(min_size, max_size)

		if self.total_size <= max_size and self.total_size >= min_size:
			print(str(self.total_size))




##############################
#######END OF CUSTOM TREE#####
##############################


def collect_file_list(lines_index, lines_len):
	file_system_list = []
	collecting_file_list = True

	while (collecting_file_list):
		temp_file = lines[lines_index]
		temp_file = temp_file.strip("\n")
		temp_file_split = temp_file.split(" ")

		if (is_split_a_command(temp_file_split)):
			collecting_file_list = False

		else:
			file_system_list.append(temp_file_split)
			lines_index += 1

			if lines_index == lines_len:
				collecting_file_list = False

	return lines_index, file_system_list

def process_file_system(file_system_list, current_direcory:CustomTree):
	# print("Found File System: ")
	# print(file_system_list)

	if current_direcory.is_init == True:
		current_direcory.print_name()
		print("WARNING! DIRECTORY HAS ALREADY BEEN LS! ")

	current_direcory.is_init = True

	for file in file_system_list:
		if file[0] == "dir":
			directory_name = file[1]
			current_direcory.directoryList.append(CustomTree(directory_name, current_direcory))
		else:
			file_name = file[1]
			file_size = int(file[0])
			current_direcory.fileList.append(CustomFile(file_name, file_size))



def traverse_tree(command_split, current_directory:CustomTree, root_directory:CustomTree):
	retVal = current_directory
	if command_split[2] == "..":
		# print("Traversing to Parent")
		# current_directory.parent.print_name()
		retVal = current_directory.parent

	elif command_split[2] == "/":
		# print("Traversing To Root")
		# root_directory.print_name()
		retVal = root_directory

	else:
		directory_name = command_split[2]
		retVal = current_directory.return_dir_by_name(directory_name)

	return retVal



def is_split_a_command(this_split):
	if this_split[0] == "$":
		return True
	return False


if __name__ == "__main__":
	input_file = open("day7.txt", "r")
	# input_file = open("day7_short.txt", "r")
	lines = input_file.readlines()

	lines_index = 0
	lines_len= len(lines)
	root_directory = CustomTree("/")

	current_directory = root_directory

	while(lines_index < lines_len):
		#Get the command
		command_line = lines[lines_index]
		command_line = command_line.strip("\n")
		command_split = command_line.split(" ")

		lines_index += 1

		if command_split[0] != "$":
			print("Broken Command: " + command_line)
			print("PROCESS COMMAND FAILED! TERMINATING PROGRAM!")
			break
		#This is a valid command
		else:
			# print(command_line)
			if command_split[1] == "ls":

				lines_index, file_system_list = collect_file_list(lines_index, lines_len)

				if len(file_system_list) >= 1:
					process_file_system(file_system_list, current_directory)

				else:
					print("WARNING! Found Empty File List!")
					current_directory.print_name()


			elif command_split[1] == "cd":
				current_directory = traverse_tree(command_split, current_directory, root_directory)

			else:
				print("Unknown Command: " + command_line)
				print("TERMINATING PROGRAM!")

	# root_directory.print_all()
	root_directory.process_sizes()
	# root_directory.find_min_sizes(100000)



	size_avalible = TOTAL_DISK_SPACE - root_directory.total_size
	size_needed = UPDATE_SIZE - size_avalible
	# print(size_needed)

	root_directory.find_size_range(size_needed, size_needed + 100000)





	