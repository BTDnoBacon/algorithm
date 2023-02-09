import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N = int(input())
def factorial(n):
    if n+1 >= N:
        return n+1
    else:
        return (n+1) * factorial(n+1)

print(factorial(0))