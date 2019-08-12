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


def trinum(n):
    value = n * (n+1) * 0.5
    return int(value)


def factorCount(n):
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
    factors.append(1)
    factors.append(n)
    factors = list(dict.fromkeys(factors))
    num_allFactors = len(factors)
    return num_allFactors, factors


# factorCount should be 2016: 36, 3240: 40, 5460: 48, 25200: 90, 73920: 112, 157080: 128

print(trinum(4006))

start = 10000
while True:
    x = factorCount(trinum(start))
    if x[0] > 500:
        print(trinum(start), x)
        break
    else:
        print(start),
        start += 1

