import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, c, d = map(int,input().split())
    quest_case = list(map(int, input().split()))
    quest_case.sort(reverse=-1)
    # print(n, c, d)
    # print(quest_case)
    if quest_case[0] > c:
        print('Infinity')
        continue
    elif quest_case[0] * d < c:
        print('Impossible')
        continue
    elif quest_case[0] * d == c:
        print(0)
        continue

    current_sum = sum(quest_case)
    print()

