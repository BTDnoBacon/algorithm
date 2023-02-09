import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())


dp_li = [0 for _ in range(101)]

dp_li[1] = dp_li[2] = dp_li[3] = 1

for _ in range(T):
    N = int(input())
    if dp_li[N] > 0 :
        print(dp_li[N])
        continue
    if N > 3:
        for i in range(4, N+1):
            dp_li[i] = dp_li[i-2] + dp_li[i-3]

    print(dp_li[N])
