'''
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def reverse(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return (n / reverse(n)) == 1

def descending_products(n):
    ''' Generates unique, descending products if the form i*j, starting with
        i = j = n
    '''
    l = [x + 1 for x in range(n)]

    while sum(l) > 0:
        prodl = [x*(i+1) for i, x in enumerate(l)]
        max_prod = max(prodl)
        max_prod_i = prodl.index(max_prod)
        l[max_prod_i] -= 1
        yield max_prod


def largest_palindrome(d):
    ''' Return largest palindrome made from product of two d-digit numbers '''
    max_num = int('9' * d)

    for p in descending_products(max_num):
        if is_palindrome(p):
            return p

    raise ValueError('No Palindrome Found')

if __name__ == '__main__':
    result = largest_palindrome(3)
    print(result)
