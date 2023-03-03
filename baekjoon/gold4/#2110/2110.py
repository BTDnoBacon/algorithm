import sys
sys.getrecursionlimit(100000)
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def binarysearch(s, l):
    global max_length
    global C

    mid = (s+l) // 2
    C -= 1
    if C > 0:
        binarysearch(mid + 1, l)
        binarysearch(s, mid-1)
    else:
        max_length = min(max_length, house[mid] - house[s], house[l] - house[mid])




N, C = map(int, input().split())

house = [int(input()) for _ in range(N)]
house.sort()


max_length = 200000
C -= 2
binarysearch(0, N-1)

print(max_length)

