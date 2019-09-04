import re
import sys


def primefind(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


primes = [item for item in list(primefind(1000000)) if item > 100000]
primes.reverse()
print("Primes generated to", primes[0])

# This bit looks for patterns in
# Index iterator for list of primes.
for i in range(len(primes)):
    # Comparing current prime to next prime.
    j = 1
    while i+j < len(primes)-1:
        diff = primes[i] - primes[i+j]
        # This should be a regex expression for any char and zeroes.
        if any(item in str(diff) for item in ['2','3','4','5','6','7','8','9']):
            j += 1
            continue
        else:
            arr = []
            score = 0
            for k in range(0, 10):
                if primes[i] - diff*k in primes:
                    arr.append(primes[i] - diff*k)
                    score += 1
            if score > 7:
                shift = len(str(primes[i])) - len(str(diff))
                indices = [l + shift for l, x in enumerate(str(diff)) if x == "1"]
                indice_test = [str(primes[i])[m] for m in indices]
                if all(x == indice_test[0] for x in indice_test):
                    print(primes[i], diff, score, arr)
            j += 1
        sys.stdout.write("\rCalculating for %s" % primes[i])
        sys.stdout.flush()


