# I drew it out and determined the following
# For i in increment (each layer)
# n = 1 + 2i
# Corners are n^2, n^2 - 2i, n^2 - 4i, n^2 - 6i
# Each layer, except i = 0, has diagonals summing to 4n^2 - 12i
# = 4(1 + 2i)^2 - 12i
# = 4(1 + 4i + 4i^2) - 12i
# = 4 + 16i + 16i^2 - 12i
# = 4 + 4i + 16i^2
# = 4(1 + i + 4i^2)

# Base i = 0
sum = 1
n_max = 1001

i_max = (n_max - 1)/2
for i in range(1, int(i_max + 1)):
    sum += 4 * (1 + i + 4 * i * i)

print(sum)