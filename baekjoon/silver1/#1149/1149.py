import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
case = [list(map(int, input().split())) for _ in range(N)]

result = [case[0][0], case[0][1], case[0][2]]

for i in range(1, N):
    a = result[0]
    b = result[1]
    c = result[2]

    result[0] = min(b+case[i][0], c+case[i][0])
    result[1] = min(a+case[i][1], c+case[i][1])
    result[2] = min(a+case[i][2], b+case[i][2])


print(min(result))

    