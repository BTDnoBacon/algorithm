import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


while True:
    dummy = list(map(int, input().split()))
    if dummy[0] == 0:
        break
    n = dummy[0]
    test_case = dummy[1:]
    # print(n, test_case)

    stack = []
    max_value = 0

    for i in range(n + 1):
        # print(stack)
        # print(max_value)
        order = i
        if i < n:
            cur = test_case[i]
        else:
            cur = -1
        while stack:
            if stack[-1][0] < cur :
                stack.append([cur, order])
                break
            # elif stack[-1][0] == cur:
            #     max_value = max(stack[-1][0] * (i - stack[-1][1]), max_value)
            #     break
            else:
                max_value = max(stack[-1][0] * (i - stack[-1][1]), max_value)
                order = stack[-1][-1]
                stack.pop()
        if len(stack) == 0:
            stack.append([cur, order])

    # print(stack)
    print(max_value)