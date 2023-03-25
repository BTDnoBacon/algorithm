N, M, K = list(map(int, input().split()))


case = {}

case[0] = 1


def func(i):
    if i == 0:
        return 1
    elif i in case.keys():
        return case[i]
    case[i] = func(i//M) + func(i//K)
    return func(i//M) + func(i//K)


print(func(N))
