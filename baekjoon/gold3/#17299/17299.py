import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


import collections

N = int(input())
case = list(map(int, input().split()))
value_case = collections.Counter()
for item in case:
    value_case[item] += 1

# print(value_case)
answer_list = []
check_case = []
check = False
for i in range(N):
    check_case.append([case[i], value_case[case[i]]])

print(check_case)

for i in range(N):
    for j in range(i+1, N):
        if check_case[i][1] < check_case[j][1]:
            answer_list.append(check_case[j][0])
            check = True
            break
        else:
            check = False
            continue

    if not check:
        answer_list.append(-1)

answer_list.append(-1)
print(*answer_list)


































# answer_list = [-1]

# current_top_left_value = value_case[case[0]]
# current_top_left_keys = case[0]

# for i in range(1, N):
#     if current_top_left_value < value_case[case[i]]:
#         answer_list.append(-1)
#     elif current_top_left_value == value_case[case[i]]:
#         current_top_left_value = value_case[case[i]]
#         current_top_left_keys = case[i]
#         answer_list.append(-1)
#     else:
#         answer_list.append(current_top_left_keys)

# print(answer_list)