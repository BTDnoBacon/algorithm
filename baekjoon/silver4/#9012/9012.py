import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    # print('---')
    test_case = list(input().rstrip())
    stack = 0
    check = False
    for item in test_case:
        if item == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            print('NO')
            check = True
            break
    if stack == 0:
        print("YES")
    elif stack != 0 and check == False:
        print('NO')
