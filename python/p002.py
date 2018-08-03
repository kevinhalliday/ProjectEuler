'''
By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
'''

def four_mil_fib():
    ''' Generate the Fibonacci sequence until values exceed four million '''

    # Start sequence with initial values
    n1 = 1
    n2 = 2
    yield n1
    yield n2

    while n1 + n2 <= 4000000:
        yield n1 + n2
        temp = n2
        n2 = n1 + temp
        n1 = temp


if __name__ == '__main__':
    result = sum(n for n in four_mil_fib() if n % 2 == 0)
    print(result)
