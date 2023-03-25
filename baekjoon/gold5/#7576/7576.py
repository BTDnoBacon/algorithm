import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

case = [list(map(int, input().split())) for _ in range(M)]
# print(case)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        # print(temp)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
                continue
            elif case[nx][ny] == 0:
                # print(case[x][y])
                case[nx][ny] = case[x][y] + 1
                queue.append([nx, ny])


queue = deque()
for i in range(M):
    for j in range(N):
        if case[i][j] == 1:
            queue.append([i, j])

bfs()

max_value = 0
check = True
for col in case:
    for item in col:
        if item == 0:
            check = False
        elif item > max_value:
            max_value = item

if not check:
    print(-1)
else:
    print(max_value - 1)
