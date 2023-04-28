import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = 0
for _ in range(N):
    building = int(input())

    while stack:
        if stack[-1] <= building:
            stack.pop()
        else:
            result += len(stack)
            stack.append(building)
            break

    if not stack:
        stack.append(building)
        continue

print(result)
