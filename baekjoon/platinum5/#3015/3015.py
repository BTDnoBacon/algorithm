import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

stack = []
count = 0
for i in range(1, N+1):
    pop_count = 0
    # print(count)
    cur = int(input())
    while stack:
        # print('----')
        # print(stack)
        if stack[-1][0] < cur:
            stack.pop()
            pop_count += 1
            count += 1
            continue
        elif stack[-1][0] == cur:
            stack.append((cur, i))
        else:
            count += i - stack[-1][1]
            count = count - pop_count
            stack.append((cur, i))
            break
    if len(stack) == 0:
            stack.append((cur, i))
            continue
    # print(stack)
    # print(count)

print(count)


        

