import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

case_a = list(input().rstrip())
case_b = list(input())
length_a = len(case_a)
length_b = len(case_b)
result = [[0 for _ in range(length_a)] for _ in range(length_b)]

# print(case_a, case_b)

count = 0
for i in range(length_b):
    for j in range(length_a):
        if case_b[i] == case_a[j]:
            count += 1
            result[i][j] = count
        else:
            result[i][j] = count

print(result)
