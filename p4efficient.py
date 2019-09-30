"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from itertools import combinations_with_replacement

def main():
	domain = []
	for i in range(100, 1000):
		domain.append(i)

	unique_multplication_list = list(combinations_with_replacement(domain, 2))

	largestPalindrome = 0
	for pair in unique_multplication_list:
			product = pair[0]*pair[1]
			if (str(product) == str(product)[::-1] and product>largestPalindrome):
				largestPalindrome = product

	print("The answer to problem 4 is: " + str(largestPalindrome) + ".")

if __name__ == "__main__":
	main()