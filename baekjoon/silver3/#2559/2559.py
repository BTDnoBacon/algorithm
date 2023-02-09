import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
case = list(map(int, input().split()))

for i in range(1, N):
    case[i] += case[i-1]

# print(case)
max_value = case[K-1]
for i in range(K, N):
    temp = case[i] - case[i-K]
    # print(temp)
    if temp > max_value:
        max_value = temp

print(max_value)