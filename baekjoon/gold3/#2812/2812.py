import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
case = list(map(int, list(input().rstrip())))
# print(N, K)
# print(case)

stack = []
for i in range(N):
    
    while K > 0:
        if len(stack) == 0:
            stack.append(case[i])
            break
        elif stack[-1] < case[i]:
            stack.pop()
            K = K - 1
            continue
        else:
            stack.append(case[i])
            break

    if K == 0 :
        stack.append(case[i])

# print(stack)
if K == 0:
    result = "".join(list(map(str, stack)))
else:
    result = "".join(list(map(str, stack[:-K])))


print(result)

    