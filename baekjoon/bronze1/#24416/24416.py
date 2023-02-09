import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())

result = [0, 0]

def fibo(n, result) :
    if n == 1 or n == 2:
        result[0] += 1
        return 1
    
    else:
        return fibo(n-1, result) + fibo(n-2, result)

fibonacci = [0 for _ in range(n+1)]

def dp(n, fibonacci):
    count = 0
    fibonacci[1] == 1
    fibonacci[2] == 1

    for i in range(3,n+1):
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
        count += 1

    return count

fibo(n, result)
result[1] = dp(n, fibonacci)

print(*result)
