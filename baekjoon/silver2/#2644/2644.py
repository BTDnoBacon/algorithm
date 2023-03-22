import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if result[i] == 0:
                result[i] = result[temp] + 1
                queue.append(i)


n = int(input())
start, end = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = [0 for _ in range(n+1)]
bfs(start)

if result[end] > 0:
    print(result[end])
else:
    print(-1)