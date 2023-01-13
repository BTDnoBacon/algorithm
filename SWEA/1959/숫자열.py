import sys
sys.stdin = open('./숫자열.txt', 'r')

N = int(input())

for order in range(1, N+1):
    A,B = input().split()
    if int(A) < int(B) :
        A_list = list(map(int, input().split()))
        B_list = list(map(int, input().split()))
        top_value = 0
        for i in range(int(B)-int(A)+1):
            sum = 0
            for j in range(int(A)):
                sum += A_list[j] * B_list[j+i]
            if top_value < sum:
                top_value = sum
        print(f'#{order} {top_value}')
    else:
        B_list = list(map(int, input().split()))
        A_list = list(map(int, input().split()))
        top_value = 0
        for i in range(int(A)-int(B)+1):
            sum = 0
            for j in range(int(B)):
                sum += A_list[j] * B_list[j+i]
            if top_value < sum:
                top_value = sum
        print(f'#{order} {top_value}')