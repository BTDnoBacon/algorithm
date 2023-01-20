import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
N_case = list(map(int, input().split()))
M = int(input())
M_case = list(map(int, input().split()))

# print(N, N_case)
# print(M, M_case)

N_case_set = set(N_case)
answer_list = []

for item in M_case:
    if item in N_case_set:
        answer_list.append(1)
    else:
        answer_list.append(0)

print(*answer_list)