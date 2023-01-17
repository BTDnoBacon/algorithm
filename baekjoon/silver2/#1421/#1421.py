import sys
sys.stdin = open('input.txt', 'r')


N, C, W = list(map(int, input().split()))

case = list()
for _ in range(N):
    case.append(int(input()))


dictionary = dict()
for item in case:
    dictionary[item] = item*W*case.count(item)

top_value = max(dictionary.values())

for i in range(1, max(case)+1):
    L = i
    check = 0
    for tree in case:
        div = 0
        if tree % L == 0:
            div = (tree // L) - 1
        else:
            div = tree // L
        
        answer = W * L * (tree // L) - div * C

        if answer > 0:
            check += answer
        else:
            continue
    top_value = max(top_value, check)


print(top_value)
