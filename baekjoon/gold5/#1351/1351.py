import sys
sys.stdin = open('./input.txt', 'r')

for i in range(5):
    N, M, K = list(map(int, input().split()))

    import collections
    case = collections.defaultdict(int)

    case[0] = 1

    def func(i):
        if case[i] != 0:
            return case[i]
        case[i] = func(i//M) + func(i//K)
        return func(i//M) + func(i//K)


    print(func(N))
