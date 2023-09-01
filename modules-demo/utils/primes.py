
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



def test_is_prime():
    test_data = { 2:True, 33:False, -13:True, 23:True, 97:True}
    for number,expected in test_data.items():
        actual= is_prime(number)
        if actual==expected:
            print(f'Test passed for {number}')
        else:
            print(f'Test failed for {number}.\texpected={expected} actual={actual}')

if __name__ == '__main__':
    test_is_prime()



