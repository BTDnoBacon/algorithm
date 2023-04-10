import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n = int(input())
    select = [0] + list(map(int, input().split()))
    visited = [False for _ in range(n+1)]
    result = 0
    for i in range(1, n+1):
        end = select[i]
        cycle = []
        cycle.append(i)
        while True:
            start = end
            end = select[start]
            if start == end:
                break
            else:
                cycle.append()

