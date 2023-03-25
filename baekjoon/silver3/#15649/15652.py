import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())


result = []
def answer(N, order):
    if order != M:
            for i in range(1, N+1):
                if order == 0:
                    result.append(i)
                    answer(N, order+1)
                    result.pop()
                elif result[order-1] > i:
                    continue
                else:
                    result.append(i)
                    answer(N, order+1)
                    result.pop()
    else:
        print(*result)

answer(N, 0)
