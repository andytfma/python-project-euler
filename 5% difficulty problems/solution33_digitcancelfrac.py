def dcfcheck(a, b):
    if b < a:
        return False
    elif a < 10 or b < 10:
        return False
    elif a == b:
        return False

    fracbig = a/b
    astr = str(a)
    bstr = str(b)
    if astr[1] == '0' or bstr[1] == '0':
        return False
    elif astr[0] == bstr[0]:
        x = int(astr[1])
        y = int(bstr[1])
    elif astr[1] == bstr[1]:
        x = int(astr[0])
        y = int(bstr[0])
    elif astr[0] == bstr[1]:
        x = int(astr[1])
        y = int(bstr[0])
    elif astr[1] == bstr[0]:
        x = int(astr[0])
        y = int(bstr[1])
    else:
        return False

    fracsmall = x/y
    if fracbig == fracsmall:
        return True


arr = []
for a in range(10, 100):
    for b in range(10, 100):
        if dcfcheck(a,b):
            arr.append([a, b])


solution = [1, 1]
for frac in arr:
    solution[0] = solution[0] * frac[0]
    solution[1] = solution[1] * frac[1]

print(solution)