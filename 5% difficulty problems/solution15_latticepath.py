
n = 20
expand = []

for i in range(1, n + 2):
    expand.append([0] * i)

expand[0][0] = 0
expand[1][0] = expand[1][1] = 1

for x in range(2, len(expand)):
    expand[x][0] = expand[x][-1] = 1
    for y in range(1, len(expand[x])-1):
        expand[x][y] = expand[x-1][y-1] + expand[x-1][y]

collapse = expand.copy()
collapse.reverse()

print(collapse)

for x in range(1, len(collapse)):
    for y in range(len(collapse[x])):
        collapse[x][y] = collapse[x-1][y] + collapse[x-1][y+1]

print(collapse)
print(collapse[-1][-1])