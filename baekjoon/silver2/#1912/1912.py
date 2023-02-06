import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
case = list(map(int, input().split()))
max_value = sum(case)
result = 0

for i in range(n):
    temp = result + case[i]
    result = max(temp, case[i])
    max_value = max(result, max_value)

print(max_value)









# max_value = max(case)

# for i in range(1, n):
#     case[i] += case[i-1]

# # print(case)

# max_temp = max(case)
# idx = case.index(max_temp)
# if idx == 0:
#     max_value = max(max_temp, max_value)
# else:
#     max_value = max(max_value, max_temp - min(case[:idx]))


# print(max_value)