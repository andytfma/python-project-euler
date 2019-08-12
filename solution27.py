def prime_test(n):
    isPrime = True
    for num in range(2, int(abs(n) ** 0.5) + 1):
        if n % num == 0:
            return False
    if isPrime:
        return True


primes = []
for possiblePrime in range(2, 1001):
    # Assume number is prime until shown it is not.
    if prime_test(possiblePrime):
        primes.append(possiblePrime)

neg_primes = [i * -1 for i in primes]


def quadratic_test(a,b):
    for n in range(0, max(a,b)+1):
        if not prime_test(n*n + a*n + b):
            return n-1


# Messy solution of storing # of primes generated in a dictionary with dict[number of primes] = [prime A, prime B],
# but if we're looking for a highest value, it should overwrite all the lower keys and leave only the highest key
# with the two solution values.
solution = {}

for prime_a in primes:
    for prime_b in primes:
        solution[quadratic_test(prime_a, prime_b)] = [prime_a, prime_b]
    for neg_prime_b in neg_primes:
        solution[quadratic_test(prime_a, neg_prime_b)] = [prime_a, neg_prime_b]
for neg_prime_a in neg_primes:
    for prime_b in primes:
        solution[quadratic_test(neg_prime_a, prime_b)] = [neg_prime_a, prime_b]


filtered = {k: v for k, v in solution.items() if k is not None}
answer = filtered[max(filtered.keys())]

print(answer[0] * answer[1])