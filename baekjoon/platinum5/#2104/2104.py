import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

case = list(map(int,input().split()))
# print(N)
# print(case)

max_value = 0
stack = []

for i in range(N):
    # print(stack)
    if len(stack) == 0:
        stack.append([case[i], case[i]])

    while stack:
        if stack[-1][0] > case[i]:
           max(max_value, stack[-1][0] * stack[-1][-1])
            


print(max_value)
