"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def main():
	sum_of_squares = 0
	sum_of_non_squares = 0
	
	for i in range(1, 101):
		sum_of_squares+=i**2
		sum_of_non_squares+=i

	difference = sum_of_non_squares**2 - sum_of_squares
	print("The answer to problem 6 is: " + str(difference) + ".")

if __name__ == "__main__":
	main()