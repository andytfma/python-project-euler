numdict = {
    0:'',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    100:'hundred'
}

def intlang(n):
    word = []
    if n == 1000:
        return ["one", "thousand"]
    elif n <= 20:
        return [numdict[n]]
    else:
        nstr = str(n)
        hundreds = True
        tens = True
        if len(nstr) <= 2:
            hundreds = False

        if hundreds == True:
            word.append(numdict[int(nstr[0])])
            word.append("hundred")
            if nstr[1] + nstr[2] != '00':
                word.append("and")
            else:
                return(word)
            slice = nstr[1:]
            nstr = slice

        if int(nstr[0])*10 + int(nstr[1]) <= 20:
            word.append(numdict[int(nstr[0])*10 + int(nstr[1])])
        elif int(nstr[1]) == 0:
            word.append(numdict[int(nstr[0])*10])
        else:
            word.append(numdict[int(nstr[0])*10])
            word.append(numdict[int(nstr[1])])

        return(word)


def countnum(n):
    nstr = ''.join(intlang(n))
    return len(nstr)


solution = 0

for i in range(1, 1001):
    print(intlang(i))
    solution += countnum(i)

print(solution)