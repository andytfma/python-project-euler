solution = []


def convert(arr):
    return int("".join([str(i) for i in arr]))


def pandigital(arr):
    global solution
    # Check for ab * cde = fghi
    multi = convert(arr[0:2]) * convert(arr[2:5])
    product = convert(arr[5:9])
    if multi == product:
        solution.append(product)
    # Check for a * bcde = fghi
    multi = convert(arr[0:1]) * convert(arr[1:5])
    product = convert(arr[5:9])
    if multi == product:
        solution.append(product)
    # ab * cd = efghi, abc * def = ghi, etc. are not possible.


nums = list(range(1, 10))

count = 0
for a in nums:
    for b in [i for i in nums if i not in [a]]:
        for c in [i for i in nums if i not in [a, b]]:
            for d in [i for i in nums if i not in [a, b, c]]:
                for e in [i for i in nums if i not in [a, b, c, d]]:
                    for f in [i for i in nums if i not in [a, b, c, d, e]]:
                        for g in [i for i in nums if i not in [a, b, c, d, e, f]]:
                            for h in [i for i in nums if i not in [a, b, c, d, e, f, g]]:
                                for i in [i for i in nums if i not in [a, b, c, d, e, f, g, h]]:
                                    pandigital([a, b, c, d, e, f, g, h, i])
                                    count += 1

print(list(dict.fromkeys(solution)))
print(sum(list(dict.fromkeys(solution))))
