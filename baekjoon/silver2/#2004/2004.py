import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

result_five = 0
result_two = 0
i = 1
while True:
    if 2**i > N:
        break
    result_five +=  (N // 5**i) - ((N-M) // 5**i) - (M//5**i)
    result_two += (N// 2**i) - ((N-M)//2**i) - (M//2**i)
    i += 1

# print(result_five, result_two)
print(min(result_five, result_two))