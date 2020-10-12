"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def main():
	# dynamic programming / lookup table must be used to solve this problem
	# dictionaries in Python are essentially look up tables or hashmaps

	lookup_table = {}
	max_number_of_terms = 0
	max_starting_number = 0
	for i in range(1, 1000000):
		number_of_terms = collatz(i, lookup_table)
		if number_of_terms > max_number_of_terms:
			max_number_of_terms = number_of_terms
			max_starting_number = i

	print("Maximum number of terms: ", max_number_of_terms, "\nStarting number which produces the maximum number of terms: ", max_starting_number)

def collatz(starting_int, lookup_table):
	counter = 1 # start counter with 1, knowing when the while loop ends, starting_int MUST == 1 and that accounts for 1 term.
	while starting_int != 1:
		counter+=1
		if starting_int not in lookup_table:
			starting_int_init = starting_int
			if starting_int % 2 == 0:
				starting_int/=2
			else:
				starting_int = 3*starting_int+1
			lookup_table[starting_int_init] = starting_int

		else:
			starting_int = lookup_table[starting_int]
	return counter


if __name__ == "__main__":
	main()