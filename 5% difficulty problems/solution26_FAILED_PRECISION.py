# https://stackoverflow.com/questions/29481088/how-can-i-tell-if-a-string-repeats-itself-in-python
import re
from decimal import *
getcontext().prec = 10000


REPEATER = re.compile(r"(.+?)\1+")


def repeated(s):
    match = REPEATER.search(s)
    return match.group(1) if match else None


fractions = []
for i in range(1, 1001):
    fract = Decimal(1.0)/Decimal(i)
    fractions.append([i, str(fract)])

repeat_dict = {}
for i in range(len(fractions)):
    if len(fractions[i][1]) > 10:
        repeat_dict[fractions[i][1]] = fractions[i][0]

solution_dict = {}
for e in repeat_dict.keys():
    sub = repeated(e)
    if sub:
        solution_dict[len(sub)] = e
        # print("%r: %r" % (e, sub))
    else:
        print("That should not have happened.")

print(max(solution_dict.keys()))
print(solution_dict[max(solution_dict.keys())])
print(repeat_dict[solution_dict[max(solution_dict.keys())]])

print(repeated(str(Decimal(1.0)/Decimal(983))))