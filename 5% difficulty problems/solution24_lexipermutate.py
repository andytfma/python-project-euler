# Brute-force program - has to be a better way to solve this.
# Better solution: could have used combinatorics! I calculated out n(x) = x * n(x-1) for permutation count, and could
# have used it to determine each digit by using %.

size = 10

test_array = [i for i in range(0, size)]


def lexi(arr):
    if len(arr) == 1:
        return [arr]
    elif len(arr) == 2:
        return [[arr[0], arr[1]], [arr[1], arr[0]]]
    else:
        arr_return = []
        for i in arr:
            arr_no_i = [thing for thing in arr if thing != i]
            for j in lexi(arr_no_i):
                arr_return.append([i] + j)
        return arr_return


print(''.join(lexi(test_array)[999999]))
