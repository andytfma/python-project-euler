import re
import sys

# Generate all primes up to certain value.
# primes = []
# for possiblePrime in range(56003, 10000000):
#     # Assume number is prime until shown it is not.
#     isPrime = True
#     for num in range(2, int(possiblePrime ** 0.5) + 1):
#         if possiblePrime % num == 0:
#             isPrime = False
#             break
#     if isPrime:
#         primes.append(str(possiblePrime))
primelist = []
def primefind(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

primelist = list(primefind(1000000))
print("Primes generated to", max(primelist))
primes = [str(i) for i in primelist]
print("Primes converted to strings.")

# Removing primes that don't have duplicated values.
# (On the assumption that you're replacing more than one value for the solution.)
r = re.compile(r"([0-9])(.*)\1")
primes_mult = []
for prime in primes:
    if r.search(prime):
        primes_mult.append(prime)

print(len(primes), len(primes_mult))

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

scores_mult = []
for prime in primes_mult:
    score = 1
    arr = [prime]
    dupe = r.search(prime).group(1)
    for num in [num for num in nums if num != dupe]:
        _ = prime.replace(dupe, num)
        if _ in primes_mult:
            arr.append(_)
            score += 1
    scores_mult.append(score)
    sys.stdout.write("\rCalculating for %s" % prime)
    sys.stdout.flush()
    if score > 7:
        print()
        print(" Found:", prime, "with", score, "matches.", arr)


