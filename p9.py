""" 
	Problem

https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

	Problem Solving

I observe that if sqrt(1000) = 31.6. Thus, c < 31, and a < b < c < 31.

The upper bound is c = 31.

The lower bound is a = 1.

We can go through permutations of a^2+b^2+c^2 under these constraints. 

With that, we can brute force a solution with ease, even if it is inefficient.

"""

def main():
	triplet = calculateTriplet()

	print("The answer to problem 9 is: " + str(triplet[0]*triplet[1]*triplet[2]) + ".")
	print("\nBonus:\nThe triplet is: " + str(triplet[0]), str(triplet[1]), str(triplet[2]) + ".")

def calculateTriplet():
	for i in range(1, 32):
		for j in range (1, 32):
			for k in range(1, 32):
				if (i**2+j**2+k**2 == 1000):
					return(i, j, k)





if __name__ == "__main__":
	main()