
def is_prime(number):
    if number<2:
        return False
    x=2
    while x<number:
        if number%x==0:
            return False
        x+=1
        
    return True

def find_primes(min,max):
    primes=[]
    number=min
    while number<max:
        if is_prime(number):
            primes.append(number)
        number+=1
    return primes

print(f'primes.py loaded as module {__name__}')




