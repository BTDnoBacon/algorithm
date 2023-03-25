import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

import math

M = int(input())

case = [int(input()) for _ in range(M)]
case.sort()
result = []
# print(case)

gcd_case = []
for i in range(1, M):
    gcd_case.append(case[i]-case[i-1])

# print(gcd_case)
temp = gcd_case[0]
# print(len(gcd_case))
for i in range(1, len(gcd_case)):
    temp = math.gcd(temp, gcd_case[i])

# print(temp)
# print(math.sqrt(temp))
for i in range(1, int(math.sqrt(temp))+1):
    if temp % i == 0:
        result.append(i)
        result.append(temp//i)


result.remove(1)
result = list(set(result))
result.sort()

print(*result)