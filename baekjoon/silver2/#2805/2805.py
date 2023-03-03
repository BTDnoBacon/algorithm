import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

case = list(map(int, input().split()))

s = 0
l = max(case)

max_height = 0

while s <= l:
    mid = (s + l) // 2
    # print(mid)

    temp_sum = 0

    for item in case:
        if item > mid:
            temp_sum += item - mid
    
    if temp_sum >= M:
        s = mid + 1
        if max_height < mid:
            max_height = mid
    else:
        l = mid - 1

print(max_height)