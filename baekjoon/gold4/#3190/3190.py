import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

location = [[0 for _ in range(N+1)] for _ in range(N+1)]

K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    # print(a, b)
    location[a][b] = 2

snake_loca = deque()
snake_loca.append([1,1])

L = int(input())
# time = []
cur_direction = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
count = 0
end = False

for _ in range(L):
    X, C = input().split()
    X = int(X)
    X = X - count
    # print(X)
    while X > 0:
        count += 1
        X -= 1
        x, y = snake_loca[-1]
        x += dx[cur_direction]
        y += dy[cur_direction]
        snake_loca.append([x, y])
        # print(x, y)
        # print(snake_loca)
        # print(location[x][y])
        # print(count)
        if x < 1 or x > N or y < 1 or y > N or location[x][y] == 1:
            end = True
            break
        elif location[x][y] == 2:
            location[x][y] = 1
            continue
        
        else:
            location[x][y] = 1
            nx, ny = snake_loca.popleft()
            location[nx][ny] = 0
            continue

    if end == True:
        print(count)
        # print(snake_loca)
        break

    if C == 'D':
        cur_direction += 1
    else:
        cur_direction -= 1
    cur_direction %= 4

while end != True:
    count += 1
    x, y = snake_loca[-1]
    x += dx[cur_direction]
    y += dy[cur_direction]
    snake_loca.append([x, y])
    # print(x, y)
    # print(snake_loca)
    # print(location[x][y])
    # print(count)
    if x < 1 or x > N or y < 1 or y > N or location[x][y] == 1:
        end = True
        print(count)

        break
    elif location[x][y] == 2:
        location[x][y] = 1
        continue
    
    else:
        location[x][y] = 1
        nx, ny = snake_loca.popleft()
        location[nx][ny] = 0
        continue

# if end == True:
#     print(count)
#     # print(snake_loca)