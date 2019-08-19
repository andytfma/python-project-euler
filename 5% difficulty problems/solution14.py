def collatz_length(n):
    counter = 0
    while True:
        if n == 1:
            counter += 1
            break
        elif n % 2 == 0:
            n = n/2
            counter += 1
        else:
            n = 3*n + 1
            counter += 1
    return counter


number = 0
length = 0
start = 1000000
for i in range(999999):
    if collatz_length(start-i) >= length:
        number = start - i
        length = collatz_length(start-i)

print(number, length)
