import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

result = 0

for num in arr:
    if num == 1:
        continue
    check = True
    for i in range(2, num//2 + 1):
        if num % i  == 0:
            check = False
            break
    if check == True:
        result += 1

print(result)
