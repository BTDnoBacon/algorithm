import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

visited = [0 for _ in range(100001)]
queue = deque()
queue.append(N)
cnt = 0
min_time = 1234567
visited[N] = 0
while queue:
    # print(queue)
    # print(visited)
    value = queue.popleft()
    if value == K:
        min_time = visited[value]
        cnt += 1
        continue

    for next in (value + 1, value - 1, value * 2):
        if 0 <= next < 100001:
            if visited[next] == 0 or visited[next] == visited[value] + 1:
                queue.append(next)
                visited[next] = visited[value] + 1

print(min_time)
print(cnt)

