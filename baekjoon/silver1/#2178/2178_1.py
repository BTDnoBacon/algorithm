import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, list(input().rstrip()))) for _ in range(N)]

# 상하 좌우 탐색을 위한 list
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 큐 생성하고, 시작위치 넣기
queue = deque()
queue.append([0, 0])

# 큐에 원소가 있는동안 반복
while queue:
    # x,y좌표 할당하기
    x, y = queue.popleft()
    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상하좌우 좌표가 범위 밖이면 continue
        if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
            continue
        # 상하좌우중 값이 1이라면 이전값을 더해주고, 좌표를 큐에 넣기
        elif matrix[nx][ny] == 1:
            matrix[nx][ny] += matrix[x][y]
            queue.append([nx, ny])

print(matrix[N-1][M-1])