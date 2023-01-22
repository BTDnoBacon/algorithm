import sys
sys.stdin = open('./input.txt', 'r')

import collections


for num in range(5):
    N = int(input())
    case = []
    for n in range(N):
        case.append(list(map(str, input())))
    order = collections.defaultdict(int)
    dp = [[0 for _ in range(N)] for _ in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if case[i][j] == 'Y' or (case[i][k] == 'Y' and case[k][j] == 'Y'):
                    dp[i][j] = 1
    for i in range(N):
        order[i] = sum(dp[i])

    print(max(order.values()))



