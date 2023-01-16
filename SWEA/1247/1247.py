import sys
sys.stdin = open('input.txt', 'r')

import collections

def dfs(start, end, case):
    dict = collections.defaultdict(int)
    queue = collections.deque()
    queue.append(start)
    




N = int(input())
for _ in range(N):
    M = int(input())
    dummy = list(map(int, input().split()))
    case = list()
    start = dummy[:2]
    end = dummy[2:4]
    for i in range(2, M+2):
        case.append(dummy[i*2:i*2+2])
    dfs(start, end, case)

    




