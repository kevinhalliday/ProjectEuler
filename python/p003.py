'''
What is the largest prime factor of the number 600851475143?
'''

def generate_primes():
    primes = []
    n = 2

    while True:
        isPrime = True
        for m in primes:
            if n % m == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(n)
            yield n
        n += 1

def largest_prime_factor(n):
    for p in generate_primes():
        if n == p:
            return n

        while n % p == 0:
            n = n/p

if __name__ == '__main__':
    result = largest_prime_factor(600851475143)
    print(result)

