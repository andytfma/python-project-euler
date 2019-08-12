arr = []

with open("./solution11.txt", 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        arr.append([int(i) for i in line.split(' ')])


def side4(x, y):
    x_ = x
    y_ = y
    product = 1
    for i in range(4):
        product = product * arr[y_][x_]
        x_ += 1
    return product


def down4(x, y):
    x_ = x
    y_ = y
    product = 1
    for i in range(4):
        product = product * arr[y_][x_]
        y_ += 1
    return product


def diag4_down(x, y):
    x_ = x
    y_ = y
    product = 1
    for i in range(4):
        product = product * arr[y_][x_]
        x_ += 1
        y_ += 1
    return product


def diag4_up(x, y):
    x_ = x
    y_ = y
    product = 1
    for i in range(4):
        product = product * arr[y_][x_]
        x_ += 1
        y_ -= 1
    return product


side_products = []
for y in range(0, 20):
    line_products = []
    for x in range(0, 17):
        line_products.append(side4(x, y))
    side_products.append(line_products)
side_largest = max([max(line) for line in side_products])
print(side_largest)

down_products = []
for y in range(0, 17):
    line_products = []
    for x in range(0, 20):
        line_products.append(down4(x, y))
    down_products.append(line_products)
down_largest = max([max(line) for line in down_products])
print(down_largest)

diag_down_products = []
for y in range(0, 17):
    line_products = []
    for x in range(0, 17):
        line_products.append(diag4_down(x, y))
    diag_down_products.append(line_products)
diag_down_largest = max([max(line) for line in diag_down_products])
print(diag_down_largest)

diag_up_products = []
for y in range(3, 20):
    line_products = []
    for x in range(0, 17):
        line_products.append(diag4_up(x, y))
    diag_up_products.append(line_products)
diag_up_largest = max([max(line) for line in diag_up_products])
print(diag_up_largest)