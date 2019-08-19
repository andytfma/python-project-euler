# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def pyth(a, b):
    c = (a*a + b*b)**(0.5)
    sum = a + b + c
    product = a*b*c
    if sum == float(int(sum)):
        if int(sum) == 1000:
            print(a, b, c, sum, product)


def BEEPBEEPscan():
    for a in range(0, 500):
        for b in range(0, 500):
            pyth(a, b)


BEEPBEEPscan()