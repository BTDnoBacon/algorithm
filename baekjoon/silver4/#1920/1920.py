import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
case = list(map(int, input().split()))
case.sort()

M = int(input())
test = list(map(int, input().split()))
# print(test)
def binary_search(n):
    s = 0
    l = N - 1
    while s <= l:
        # print(s, l)
        mid = (s+l)//2
        if case[mid] == n:
            return 1
        elif case[mid] < n:
            s = mid + 1
            continue
        else:
            l = mid - 1
    
    return 0

for item in test:
    print(binary_search(item))