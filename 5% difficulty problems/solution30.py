# Checks if n number is the sum of the xth power of its digits.
def digitpower(n,x):
    arr = [int(digit) ** x for digit in str(n)]
    if n == sum(arr):
        return True
    else:
        # print(sum(arr))
        return False


# Running the checker on an arbitrarily large number seems to show that digit fifth power sums don't really go higher
# than 6 digits in sum length, so I'll cap the range at 999999.
print(digitpower(999999999, 5))

solution = []
for n in range(2, 999999):
    if digitpower(n, 5):
        print(n)
        solution.append(n)

print(sum(solution))