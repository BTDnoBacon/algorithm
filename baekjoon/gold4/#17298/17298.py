import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
case = list(map(int, input().split()))
# print(case)

stack = []
result = [0 for _ in range(N)]
for i in range(N):
    cur = case[i]

    while stack:
        if stack[-1][0] >= cur:
            stack.append([cur, i])
            break
        else:
            result[stack[-1][1]] = cur
            stack.pop()
            continue
    if len(stack) == 0:
        stack.append([cur, i])

while stack:
    result[stack.pop()[1]] = -1

print(*result)
        