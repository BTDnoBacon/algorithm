import sys
sys.stdin = open('input.txt', 'r')

import functools

S, K = list(map(int, input().split()))

case = [S//K for _ in range(K)]

if S % K != 0:
    for i in range(S%K):
        case[i] += 1

print(functools.reduce(lambda x, y: x*y, case))