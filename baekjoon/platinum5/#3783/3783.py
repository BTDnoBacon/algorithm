import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def binarysearch(n):
    n = n * 10**10
    s = n * 10**3
    l = n * 10**4
    while s < l:
        # print(s,l)
        mid = (s+l)//2
        temp = mid**3
        if -1 <= temp - n <= 1:
            print(mid)
            return mid

        elif temp > n:
            l = mid-1
        else:
            s = mid+1
    return mid-1


T = int(input())
for _ in range(T):
    print(binarysearch(int(input())))

