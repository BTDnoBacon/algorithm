import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# import collections

t = int(input())


# def subtract(s):
#     check = test_case[:s] + test_case[s+1:]
#     # print(check)
#     return test_case[s] - max(check)


for _ in range(t):
    n = int(input())
    test_case = [item for item in list(map(int, input().split()))]
    # for item in list(map(int, input().split())):
    #     test_case.append(item)
    # result = []
    # print(test_case)
    max_value = max(test_case)
    max_two_value = sorted(test_case)[-2]
    # print(max_two_value)
    # print(test_case)
    for i in range(n):
        answer = test_case[i]
        if answer == max_value:
            print(answer - max_two_value, end=' ')
        else:
            print(answer - max_value, end=' ')
        

    print('', end='\n')

    # print(*result)
