'''
What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
'''

from functools import reduce
from math import gcd

def lcm(a,b):
    ''' Returns least common multiple of a and b '''
    return a*b // gcd(a,b)

def smallest_multiple(l):
    ''' Returns the smallest positive number that is evenly divisible by
        all of the numbers in the provided list l
    '''
    return reduce(lcm, l)

if __name__ == '__main__':
    result = smallest_multiple(list(range(1,20+1)))
    print(result)
