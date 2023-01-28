import sys
import collections
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    test_case = collections.deque(item for item in list(map(int, input().split())))
    # print(test_case)

    stack = []
    check_down = True
    check_up = True

    while test_case:
        case = test_case.popleft()
        if len(stack) == 0:
            # [이전값, 계곡 체크, 현재 계곡 수]
            stack.append([case, 0, 0])
            continue
        if stack[-1][0] <= case and stack[-1][1] == 0:
            stack.append([case, 0, 0])
            continue
        elif stack[-1][0] >= case and stack[-1][2] == 0:
            stack.append([case, 1, 0])
            continue
        elif stack[-1][0] <= case:
            stack.append([case, 1, 1])
            continue
        elif stack[-1][0] > case:
            break
        
    # print(stack)
    if len(test_case) != 0 or (stack[-1][1] == 1 and stack[-1][2] != 1):
        print('NO')
    else:
        print('YES')



    # print(stack)



