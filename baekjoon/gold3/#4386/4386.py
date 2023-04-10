import sys
import math
input = sys.stdin.readline

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
stars.sort(key=lambda x:(x[0], x[1]))
stars += [[3000, 3000]]
print(stars)


MST = math.sqrt((stars[1][0] - stars[0][0])**2 + (stars[1][1] - stars[0][1])**2)

# if n > 4:
idx = 1
while idx < n - 1:
    A = math.sqrt((stars[idx+1][0] - stars[idx][0])**2 + (stars[idx+1][1] - stars[idx][1])**2)
    B = math.sqrt((stars[idx+2][0] - stars[idx+1][0])**2 + (stars[idx+2][1] - stars[idx+1][1])**2)
    if A <= B:
        MST += A
        idx += 1
    else:
        MST += B
        idx += 2

print(idx)
print(round(MST, 2))
