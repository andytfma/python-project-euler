def factorial(n):
    n_fact = 1
    for i in range(1, n+1):
        n_fact = n_fact * i
    return n_fact


solution = str(factorial(100))

print(sum([int(i) for i in solution]))