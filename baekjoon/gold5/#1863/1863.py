import sys
input = sys.stdin.readline

n = int(input())

stack = []
stack.append([0, 0])
result = 0
for i in range(n+1):
    dummy = list(map(int, input().split())) if i < n else [1000001, 0]
    # print(stack, dummy, result, '시작')
    if len(stack) == 0:
        stack.append(dummy)
        continue
    if stack[-1][1] < dummy[1]:
        stack.append(dummy)
    else:
        while stack and stack[-1][1] > dummy[1]:
            # print(stack, result)
            temp = stack.pop()
            if temp[1] != stack[-1][1]:
                result += 1
                break
        stack.append(dummy)

print(result)
