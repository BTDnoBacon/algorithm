import sys
sys.stdin = open('input.txt', 'r')

N, L = list(map(int, input().split()))

sum = 0
for i in range(L):
    sum += i

for i in range(L, 102):
    L = i
    if N-sum < 0 or i > 100:
        print(-1)
        break
    if (N-sum) % L == 0:
        case = [(N-sum)//L + j for j in range(L)]
        answer = str()
        for row in case:
            answer += str(row)+" "
        print(answer)
        break
    sum += i