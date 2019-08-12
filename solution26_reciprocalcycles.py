import re
REPEATER = re.compile(r"(.+?)\1+$")


def repeated(s):
    match = REPEATER.match(s)
    return match.group(1) if match else 0


def div_rem(n, div):
    rem_chain = 0
    for i in range(div*2):
        leftover = n % div
        if leftover == 0:
            return 0
        else:
            rem_chain = rem_chain * 10
            if n/div < 1:
                n = leftover * 10
            else:
                n = leftover * 10
                rem_chain += leftover
    sub = repeated(str(rem_chain))
    if sub:
        return len(sub)
    else:
        return 0


arr = []

nums = list(range(1, 1001)[::-1])
for i in nums:
    arr.append(div_rem(1, i))
print(nums[arr.index(max(arr))])