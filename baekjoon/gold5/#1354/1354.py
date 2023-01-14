import sys
import collections

sys.stdin = open('./input.txt', 'r')

for i in range(4):
    N, P, Q, X, Y = list(map(int, input().split()))

    case = collections.defaultdict(int)

    case[0] = 1
    def func(i):
        if i <= 0:
            return 1
        elif i in case.keys():
            return case[i]
        case[i] = func(i//P - X) + func(i//Q - Y)
        return func(i//P - X) + func(i//Q - Y)


    print(func(N))