arr = []

# Works with both 18 and 67.
with open("./solution67.txt", 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        arr.append([int(i) for i in line.split(' ')])

arr.reverse()

max_path = [[0 for value in row] for row in arr]

max_path[0] = arr[0]

for x in range(1, len(arr)):
    for y in range(len(arr[x])):
        max_path[x][y] = max(arr[x][y] + max_path[x-1][y], arr[x][y] + max_path[x-1][y+1])

# print(arr)
# print(max_path)

print(max_path[-1][-1])