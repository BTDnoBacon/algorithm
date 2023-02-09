import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

case = [0 for _ in range(M)]

for i in range(M):
    case[i] = set(input().split())

# result = set()
count = 0
for i in range(M):
    for j in range(i+1, M):
        # if i == j:
        #     continue

        if len(case[i].union(case[j])) == 3:
            count += 1

print(N*(N-1)*(N-2)//6 - (N-2)*M + count)
