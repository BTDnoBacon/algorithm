import sys
input = sys.stdin.readline

M = int(input())
N = int(input())

prime = -1
prime_check = False
prime_arr = list()

for num in range(M, N+1):
    if num == 1:
        continue
    check = True
    for i in range(2, num//2 + 1):
        if num % i == 0:
            check = False
            break
    if check == True:
        if prime_check == False:
            prime = num
            prime_check = True
        prime_arr.append(num)

if len(prime_arr) > 0:
    print(sum(prime_arr))

print(prime)
