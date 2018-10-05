'''
What is the 10,001st prime number?
'''

from p003 import generate_primes

def nth_prime(n):
    i = 0
    prime_gen = generate_primes()

    while i < n:
        p = next(prime_gen)
        i += 1

    return p

if __name__ == '__main__':
    result = nth_prime(10001)
    print(result)
