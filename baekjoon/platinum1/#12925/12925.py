import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

T = int(input())

def cut(A):
    return [[A[0][0]%1000,A[0][1]%1000],[A[1][0]%1000,A[1][1]%1000]]
linear = [[6, -4], [1, 0]]
def generate_func(n):
    if n == 1:
        return linear
    r = generate_func(n//2)

    if n % 2 == 0:
        return cut([[r[0][0]*r[0][0] + r[0][1]*r[1][0], r[0][0]*r[0][1] + r[0][1]*r[1][1]],[r[1][0]*r[0][0] + r[1][1]*r[1][0], r[1][0]*r[0][1] + r[1][1]*r[1][1]]]) 
    else:
        return cut([[6*(r[0][0]*r[0][0] + r[0][1]*r[1][0])+r[0][0]*r[0][1] + r[0][1]*r[1][1],(-4)*(r[0][0]*r[0][0] + r[0][1]*r[1][0])],[6*(r[1][0]*r[0][0] + r[1][1]*r[1][0])+r[1][0]*r[0][1] + r[1][1]*r[1][1], (-4)*(r[1][0]*r[0][0] + r[1][1]*r[1][0])]])


# print(generate_func(5))



for i in range(1, T+1):
    print(f'Case #{i}:', end=" ")
    dummy = generate_func(int(input())-1)[0]
    result = (dummy[0]*6 + dummy[1]*2 - 1) % 1000
    print(str(result).zfill(3))