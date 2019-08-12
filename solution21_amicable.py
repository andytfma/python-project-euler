import math

# Prime factorization (Sieve) code from https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
def primeFactors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(int(i))
            n = n / i

    if n > 2:
        factors.append(int(n))
    return factors


def allFactors(n):
    factors = primeFactors(n)
    while True:
        _ = factors.copy()
        for factor in factors:
            for j in factors:
                newvalue = factor*j
                if newvalue not in factors and n % newvalue == 0:
                    factors.append(newvalue)
        if _ == factors:
            break
    if n in factors:            # BAD SOLUTION - THIS IS A HACK
        factors.remove(n)
    factors.append(1)
    factors = list(dict.fromkeys(factors))
    factors.sort()
    return factors


def d(n):
    return sum(allFactors(n))


all_pairs = []
rev_pairs = []
ami_pairs = []

for i in range(1, 10001):
    match = [i, d(i)]
    all_pairs.append(match)

print("Found d(n) for n in (1, 10000)")

for pair in all_pairs:
    rev_pairs.append([pair[1], pair[0]])

for pair in rev_pairs:
    if pair in all_pairs:
        if pair[0] != pair[1]:
            ami_pairs.append(pair)

print(ami_pairs)


solution = []

for pair in ami_pairs:
    solution.append(pair[0])
    solution.append(pair[1])

print(solution)
solution2 = list(dict.fromkeys(solution))

print(solution2)
print(sum(solution2))
