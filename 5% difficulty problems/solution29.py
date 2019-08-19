# Given a, b, returns array of all distinct a^b values.
def distinct_powers(a, b):
    arr = []
    for i in range(2, a+1):
        for j in range(2, b+1):
            arr.append(i**j)
    arr = list(dict.fromkeys(arr))
    return arr


print(len(distinct_powers(100, 100)))
# I feel like this was a little too short... or I was supposed to have done some math here to simplify the problem...
