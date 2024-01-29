myDict = {'ravi': 10, 'rajnish': 9,
		'sanjeev': 15, 'yash': 2, 'suraj': 32}

myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}

print(sorted_dict)

#Second way
# Function calling
def dictionary():
	# Declare hash function
	key_value = {}

# Initializing value
	key_value[2] = 56
	key_value[1] = 2
	key_value[5] = 12
	key_value[4] = 24
	key_value[6] = 18
	key_value[3] = 323

	print("Task 1:-\n")

	print("key_value", key_value)

	# iterkeys() returns an iterator over the
	# dictionary’s keys.
	for i in sorted(key_value.keys()):
		print(i, end=" ")


def main():
	# function calling
	dictionary()


# Main function calling
if __name__ == "__main__":
	main()

