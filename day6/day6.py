def is_start_signal_found(signal_string, message_size):
	start_index = 0
	for signal in signal_string[0:MESSAGE_SIZE-1]:
		for signal2 in signal_string[start_index+1:message_size]:
			# print(signal + signal2)
			if signal == signal2:
				return False
		start_index += 1
	return True



if __name__ == "__main__":
	input_file = open("day6.txt", "r") 
	# input_file = open("day6_short.txt", "r") 
	lines = input_file.readlines()

	MESSAGE_SIZE = 14

	num_chars_read = 0
	key_string = ""
	for line in lines:
		line = line.strip("\n")
		for char in line:
			key_string += char
			num_chars_read += 1

			if num_chars_read >= MESSAGE_SIZE:
				start_signal_found = is_start_signal_found(key_string, MESSAGE_SIZE)#Check to see if we found it.

				if start_signal_found:
					print("FOUND START SIGNAL AT INDEX: " + str(num_chars_read))
					# print(key_string)
					break
				else:
					# print(key_string)
					key_string = key_string[1:MESSAGE_SIZE+1]
					# print(key_string)
		
