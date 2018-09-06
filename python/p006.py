'''
Find the difference between the sum of squares of the first one hundred
natural numbers and the square of sum.
'''

def sum_of_squares(n):
    return sum([x**2 for x in range(1,n+1)])

def square_of_sums(n):
    return sum(range(1,n+1))**2

if __name__ == '__main__':
   result = square_of_sums(100) - sum_of_squares(100)
   print(result)
