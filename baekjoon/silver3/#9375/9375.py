import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


import collections

N = int(input())


for _ in range(N):
    T = int(input())
    test_case = collections.defaultdict(list)
    name_set = set()
    for _ in range(T):
        wear, location = map(str, input().split())
        test_case[location].append(wear)
        name_set.add(location)
    # print(test_case)

    name_list = list(name_set)
    result = 1
    for item in name_list:
        result *= (len(test_case[item])+1)


    print(result - 1)