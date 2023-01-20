import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

poke_list = []
poke_dict = {}
answer_list = list()


for _ in range(N):
    poke_list.append(input().rstrip())

for i in range(1, N+1):
    poke_dict[poke_list[i-1]] = i

    
poke_set = set(poke_list)
for _ in range(M):
    input_poke = input().rstrip()

    if input_poke in poke_set:
        answer_list.append(poke_dict[input_poke])
    else:
        answer_list.append(poke_list[int(input_poke) - 1])

for item in answer_list:
    print(item)