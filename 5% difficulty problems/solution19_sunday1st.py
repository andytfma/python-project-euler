noleap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


weekdays = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']

solution = 0
year = 1901
month = 0
dotw = 1

while year < 2001:
    if year % 4 == 0:
        monthdays = leap.copy()
    else:
        monthdays = noleap.copy()

    for month in range(1, len(monthdays)+1):
        for day in range(1, monthdays[month-1]+1):
            if (dotw == 6 and day == 1):
                print(weekdays[dotw], year, month, day)
                solution += 1

            if dotw == 6:
                dotw = 0
            else:
                dotw += 1

    year += 1

print(solution)