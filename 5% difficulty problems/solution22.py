def wordscore(word):
    alphabet = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    alphadict = dict(zip(alphabet, [i+1 for i in range(len(alphabet))]))
    finalscore = 0
    for letter in word:
        finalscore += alphadict[letter]
    return finalscore


with open("./solution22_names.txt", 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        line = line.replace('"', '')
        string = line

names = string.split(',')
names.sort()

score_rank = [i+1 for i in range(len(names))]
score_name = [wordscore(name) for name in names]

arr = []
for i in range(len(score_rank)):
    score = score_rank[i] * score_name[i]
    arr.append(score)

print(sum(arr))