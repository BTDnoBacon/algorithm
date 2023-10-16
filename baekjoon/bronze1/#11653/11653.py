import sys
input = sys.stdin.readline

N = int(input())

prime = 2

while prime <= N:
    if N % prime == 0:
        print(prime)
        N //= prime
    else:
        prime += 1
