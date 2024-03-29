# Sum square difference
#
# Problem 6
# The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

nums = [i for i in range(1, 101)]

pt1 = sum([i*i for i in nums])

num_sum = sum(nums)
pt2 = num_sum * num_sum

print("Answer 6:", pt2-pt1)

# 10001st prime
#
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

primes = []
for possiblePrime in range(2, 150000 + 1):
    # Assume number is prime until shown it is not.
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(possiblePrime)

print("Answer 7:", primes[10000])

# Largest product in a series
#
# Problem 8
# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.#
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

import re

num = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace('\n', '')

search = re.findall(r"[456789]{13}", num)
print(search)

answers = []
for result in search:
    _ = 1
    list_ = [int(char) for char in result]
    for i in list_:
        _ = _*i
    answers.append(_)

print(max(answers))