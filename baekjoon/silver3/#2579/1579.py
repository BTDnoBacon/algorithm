import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

stair = [0 for _ in range(N)]

for i in range(N):
    stair[i] = int(input())

# print(stair)

result = [0 for _ in range(N)]

result[0] = [0, stair[0]]
if N > 1:
    result[1] = [stair[1], stair[0]+stair[1]]

if N > 2:
    for i in range(2, N):
        result[i] = [stair[i]+result[i-2][1], stair[i] + result[i-1][0]]

if N > 2:
    max_value = max(result[N-1][0], result[N-1][1], stair[N-1] + result[N-3][0])
elif N == 2:
    max_value = stair[0]+stair[1]
else:
    max_value = stair[0]

print(max_value)
print(result)