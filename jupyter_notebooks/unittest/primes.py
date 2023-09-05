
def is_prime(n):
    '''
    Checks if a given number is prime or not

    >>> is_prime(5)
    True
    >>> is_prime(9)
    False
    >>> is_prime(2)
    True
    >>> is_prime(1)
    False
    '''

    if n<2:
        return False

    for x in range(2,n):
        if n%x==0:
            return False
        
    return True


def prime_count(min,max):
    '''
    counts total prime in the given range
    >>> prime_count(2,100)
    25
    >>> prime_count(-100,100)
    25
    >>> prime_count(50,100)
    10
    '''

    count=0
    for x in range(min,max):
        if is_prime(x):
            count+=1
    return count


if __name__ == '__main__':
    import doctest
    doctest.testmod()