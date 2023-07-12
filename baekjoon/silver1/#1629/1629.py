import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

A, B, C = map(int, input().split())

A = A % C

def multi(a, b):
    dummy = a * b
    return dummy % C

def div(a, b):
    if b == 1:
        return a
    new_A = div(a, b//2)
    if b % 2 == 0:
        return multi(new_A, new_A)
    else:
        return multi(multi(new_A, new_A), a)


print(div(A, B))