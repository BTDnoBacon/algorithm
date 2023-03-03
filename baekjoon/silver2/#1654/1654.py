import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

K, N = map(int, input().split())

case = [int(input().rstrip()) for _ in range(K)]

s = 1
l = max(case)
max_length = 0

while s <= l:
    mid = (s + l) // 2
    temp_sum = 0

    for item in case:
        temp_sum += item // mid
    
    if temp_sum >= N:
        s = mid + 1
        if max_length < mid:
            max_length = mid
    else:
        l = mid - 1

print(max_length)