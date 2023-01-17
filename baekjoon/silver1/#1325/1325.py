import sys
sys.stdin = open('input.txt', 'r')

import collections

N, M = list(map(int, input().split()))

case = [[0 for _ in range(N)] for _ in range(N)]
# dictionary = collections.defaultdict(str)

answer_string = ''

for _ in range(M):
    x, y = list(map(int, input().split()))
    case[y-1][x-1] = 1

# sum_case = [sum(case[k]) for k in range(N)]
top_value = 0
trust_num = 0

for i in range(N):
    trust_num = sum(case[i])
    if trust_num == 0:
        continue
    for j in range(N):
        if case[i][j] == 0:
            continue
        else:
            trust_num += sum(case[j])
    if top_value < trust_num:
        answer_string = f'{i+1}'
        top_value = trust_num
    elif top_value == trust_num:
        answer_string += f' {i+1}'
    else:
        pass

print(answer_string)

# for i in range(N):
#     trust_num = sum(case[i])
#     if trust_num > 0:
#         for j in range(N):
#             if case[i][j] == 0:
#                 continue
#             else:
#                 trust_num += sum_case[j]
#     dictionary[trust_num] += str(i+1)+" "

# max_key = max(dictionary.keys())

# print(dictionary[max_key])
            


