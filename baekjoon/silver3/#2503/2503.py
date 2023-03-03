import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input().rstrip())
minhyeok = [list(map(int, input().split())) for _ in range(N)]
# print(minhyeok)

permutation = []
dummy = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(9):
    dummy[0], dummy[i] = dummy[i], dummy[0]
    for j in range(1, 9):
        dummy[1], dummy[j] = dummy[j], dummy[1]
        for k in range(2, 9):
            dummy[2], dummy[k] = dummy[k], dummy[2]
            permutation.append(dummy[:3])
            dummy[2], dummy[k] = dummy[k], dummy[2]
        dummy[1], dummy[j] = dummy[j], dummy[1]
    dummy[0], dummy[i] = dummy[i], dummy[0]

count = 0
while permutation:
    maybe = permutation.pop()
    check = 0
    for item in minhyeok:
        speaking = str(item[0])
        strike = 0
        ball = 0
        for i in range(3):
            if int(speaking[i]) == maybe[i]:
                strike += 1
            elif str(maybe[i]) in speaking:
                ball += 1
        if strike == item[1] and ball == item[2]:
            check += 1
    if check == len(minhyeok):
        count += 1

print(count)