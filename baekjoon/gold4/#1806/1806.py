import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, S = map(int, input().split())

case = list(map(int ,input().split()))

# for i in range(1, N):
#     case[i] += case[i-1]
# print(case)

min_idx = N + 1

# for i in range(N):
#     for j in range(i, i + max_idx):
#         if j == N:
#             break
#         temp = case[j] - case[i]
#         length = j - i
#         if temp >= S and length < max_idx:
#             max_idx = length

dummy = 0
right = 0
left = 0
while True:
    if dummy >= S:
        min_idx = min(min_idx, right - left)
        dummy -= case[left]
        left += 1
    elif right == N:
        break
    else:
        dummy += case[right]
        right += 1

if min_idx == N+1:
    print(0)
else:
    print(min_idx)

            