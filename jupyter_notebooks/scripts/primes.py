import sys

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


if __name__ == "__main__":
    args = sys.argv[1:]
    if(len(args)==1):
        number=int(args[0])
        print(f"{number} is {'' if is_prime(number) else 'not'} prime")
    elif(len(args)>1):
        min=int(args[0])
        max=int(args[1])
        primes=find_primes(min,max)
        for prime in primes:
            print(prime)
    else:
        print(f"HELP: we can use this in two ways")
        print(f'check if a number is prime or not :  python primes number')
        print(f'find all primes in a range :  python primes min max')
        