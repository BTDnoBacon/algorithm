import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    user_input = deque(input().rstrip())
    n = int(input())
    dummy = input().rstrip().replace('[', '').replace(']', '').replace(',', ' ')
    test_case = deque(map(int, dummy.split()))
    # print(dummy)

    error_check = False
    first_out = True
    while user_input:
        temp = user_input.popleft()
        if temp == 'R':
            if first_out:
                first_out = False
            else:
                first_out = True

        elif len(test_case) == 0:
            error_check = True
            break

        else:
            if first_out:
                test_case.popleft()
            else:
                test_case.pop()

    if not first_out:
        result = []
        while test_case:
            result.append(test_case.pop())
    else:
        result = list(test_case)


    if error_check:
        print('error')
    else:
        print(str(result).replace(' ',''))




