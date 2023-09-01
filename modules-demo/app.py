import utils.primes
import utils.stats.histogram as h


min = int(input('min?'))
max = int(input('max?'))

result = utils.primes.find_primes(min,max)

for value in result:
    print(value, end= '\t')


