def divisor(x):
    num = 0
    for i in range(1,x):
        if x % i == 0:
            num += 1
    num += 1  # for x itself
    return num


def triangle(x):  # Where x is the number of triangle numbers to be generated.
    trianglenumbers = []
    for i in range(1, x+1):
        if i == 1:
            trianglenumbers.append(1)
        else:
            trianglenumbers.append(i + trianglenumbers[i-2])
    return trianglenumbers


numbers = 800
num_dict = {}


for i in triangle(numbers):
    num_dict[i] = divisor(i)


# triangledict goes back and adds an index for the triangle numbers because I forgot to add that earlier
triangledict = {}
counter = 1
for i in num_dict:
    triangledict[i] = counter
    counter += 1

# increase stores only triangle values where a new highest divisor # is found
increase = {}
highest_factor = 0
for i in num_dict:
    if num_dict[i] > highest_factor:
        increase[i] = num_dict[i]
        highest_factor = num_dict[i]

print(increase)


# This is where the code gets REALLY jank
# using triangledict to see at which index of triangle numbers the highest divisor #s are being found at
# also plotting because i have no idea how to solve this problem since i suck at math


plot_trivalues = list(increase.keys())
plot_triindex = [triangledict[i] for i in plot_trivalues]
plot_divisors = list(increase.values())


# import matplotlib.pyplot as plt
# plt.plot(plot_trivalues, plot_divisors, 'ro')
# plt.show()