import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    case = [list(map(int, input().split())) for _ in range(N)]
    case.sort()
    top = 0
    result = 1

    for i in range(1, N):
        if case[i][1] < case[top][1]:
            top = i
            result += 1
    print(result)