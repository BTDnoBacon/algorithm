import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def backtracking(x, y, direction):
    global count
    if x == N-1 and y == N-1:
        count += 1
        return
    elif x > N-1 or y > N-1:
        return
    elif direction == 1:
        if status[x][y+1] == 0:
            backtracking(x, y+1, 1)
        if status[x][y+1] == 0 and status[x+1][y+1] == 0 and status[x+1][y] == 0:
            backtracking(x+1, y+1, 2)
    elif direction == 2:
        if status[x][y+1] == 0:
            backtracking(x, y+1, 1)
        if status[x+1][y] == 0:
            backtracking(x+1, y, 3)
        if status[x][y+1] == 0 and status[x+1][y+1] == 0 and status[x+1][y] == 0:
            backtracking(x+1, y+1, 2)
    elif direction == 3:
        if status[x+1][y] == 0:
            backtracking(x+1, y, 3)
        if status[x][y+1] == 0 and status[x+1][y+1] == 0 and status[x+1][y] == 0:
            backtracking(x+1, y+1, 2)



N = int(input())
status = [list(map(int, input().split())) + [1] for _ in range(N)]
status.append([1 for _ in range(N+1)])
# print(status)
count = 0
backtracking(0, 1, 1)
print(count)