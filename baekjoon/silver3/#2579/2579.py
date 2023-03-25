import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

stair = [0 for _ in range(N+1)]
result = [0 for _ in range(N+1)]

for i in range(1,N+1):
    stair[i] = int(input())

# print(stair)

result = [0 for _ in range(N+1)]

if N == 1:
    print(stair[1])

if N == 2:
    print(stair[1] + stair[2])

if N > 2:
    result[1] = stair[1]
    result[2] = stair[1] + stair[2]
    for i in range(3, N+1):
        result[i] = max(result[i-2]+stair[i], result[i-3]+stair[i-1]+stair[i])

    print(result[-1])





# print(result)