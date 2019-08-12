arr = []

with open("./solution13.txt", 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        arr.append(int(line))

bignum = 0

for num in arr:
    bignum += num

print(bignum)