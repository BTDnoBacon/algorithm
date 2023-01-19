import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

case = [list(map(int, input().split()))]
case_order = [1]


for _ in range(N-1):
    [x, y] = list(map(int, input().split()))
    order = 1
    for i in range(len(case)):
        a, b = case[i]
        if x > a and y > b:
            case_order[i] += 1
        elif x < a and y < b:
            order += 1
        else:
            continue
    case.append([x, y])
    case_order.append(order)

# print(case)
print(*case_order)

