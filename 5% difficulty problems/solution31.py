arr = [1, 2, 5, 10, 20, 50, 100, 200]
N = 200

m = len(arr)

count = [0 for i in range(N + 1)]
count[0] = 1

# Count ways for all values up to 'N' and store the result
for i in range(m):
    for j in range(1, N + 1):
        if arr[i] <= j:
            count[j] += count[j - arr[i]]

print(count[N])

