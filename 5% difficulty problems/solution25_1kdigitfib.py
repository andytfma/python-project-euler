
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibs[n-1] + fibs[n-2]


fibs = []

i = 0
while True:
    lastfib = fib(i)
    fibs.append(lastfib)
    print(i, fibs[i])
    if len(str(lastfib)) == 1000:
        print()
        print(i+1)  # PE asks for true index from 1.
        break
    else:

        i += 1

