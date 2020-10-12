"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
See large_num.txt for the numbers.
"""

def main():
	large_num_sum = 0
	large_num_file = open("large_num.txt", "r")
	for line in large_num_file:
		large_num_sum+=int(line)

	print("Large number sum: ", large_num_sum)	
	print("First 10 digits of large number sum: ", str(large_num_sum)[0:10])

if __name__ == "__main__":
	main()