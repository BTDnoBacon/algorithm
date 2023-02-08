import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

case = list(map(int, input().split()))
count = [0 for _ in range(M)]
count[case[0] % M] += 1
for i in range(1, N):
    case[i] += case[i-1]
    count[case[i] % M] += 1

result = count[0]
# print(count)
for item in count:
    result += item * (item-1) // 2

print(result)