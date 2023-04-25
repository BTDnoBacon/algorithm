import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    case = [list(map(int, input().split())) for _ in range(n+2)]
    # print(case)
    check = True
    for i in range(1, n+2):
        if abs(case[i][0] - case[i-1][0]) + abs(case[i][1] - case[i-1][1]) > 1000:
            check = False
            break

    if check:
        print('happy')
    else:
        print('sad')

