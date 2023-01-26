import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

T = int(input())

def generate_func(n):
    if n == 0:
        return 2
    elif n == 1:
        return 6
    
    linear = [[6, -4], [1, 0]]
    new_linear = [[6, -4], [1, 0]]
    for _ in range(n - 2):
        new_linear[0] = [new_linear[0][0]*linear[0][0] + new_linear[0][1]*linear[1][0],new_linear[0][0]*linear[0][1]]
        new_linear[1] = [new_linear[1][0]*linear[0][0], 0]



    return new_linear[0][0]*6 + new_linear[0][1]*2

# print(generate_func(5))



for i in range(1, T+1):
    print(f'Case #{i}:', end=" ")
    dummy = (generate_func(int(input())) - 1) % 1000
    if dummy == 0:
        print('000')
    elif dummy < 10:
        print('00', end='')
        print(dummy)
    elif dummy < 100:
        print('0', end='')
        print(dummy)
    else:
        print(dummy)