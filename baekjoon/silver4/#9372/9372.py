import sys
input = sys.stdin.readline

def Find_set(x):
    while rep[x] != x:
        x = rep[x]
    return x

def Union(x, y):
    rep[Find_set(y)] = Find_set(x)

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    rep = [i for i in range(N+1)]
    cnt = 0
    for _ in range(M):
        x, y = map(int, input().split())
        Union(x, y)
    for i in range(1, N+1):
        if i != rep[i]:
            cnt += 1
    print(cnt)