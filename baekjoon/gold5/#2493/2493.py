import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

tower_list = list(map(int, input().split()))
# print(tower_list)

answer = [0]
stack = []
stack.append((tower_list[0], 0))

for i in range(1, N):
    while stack:
        if stack[-1][0] >= tower_list[i]:
            answer.append(stack[-1][1] + 1)
            stack.append((tower_list[i], i))
            break
        else:
            stack.pop()
            continue

    if len(stack) == 0:
        answer.append(0)
        stack.append((tower_list[i], i))


print(*answer)
