import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
case = list(map(int, list(input().rstrip())))
# print(N, K)
# print(case)

stack = []
count = 0
for i in range(N):
    item = case[i]

    while stack:
        if count == K:
            break
        

        if stack[-1][0] < item:
            temp = count + stack[-1][1]
            if temp > count:
                stack[-1][1] -= 1
                count += 1
                continue
            else:
                count = temp
                stack.pop()
                continue
        elif stack[-1][0] == item:
            stack[-1][1] += 1
            break
        elif stack[-1][0] > item:
            if count < K and i == N-1:
                # count += 1
                break
            else:
                stack.append([item, 1])
                break

    # print(stack)
    if len(stack) == 0 or count == K:
        stack.append([item, 1])

# print(stack)
if N != K:
    result = str()
    for row in stack:
        result += str(row[0])*row[1]

    print(result)
else:
    print(0)