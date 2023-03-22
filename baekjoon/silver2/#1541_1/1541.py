import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

result = 0
li = input().split('-')
for i in range(len(li)):
    if '+' in li[i]:
        dummy = li[i].split('+')
        # print(dummy)
        value = sum(map(int, dummy))
    else:
        value = int(li[i])
    
    if i == 0:
        result += value
    else:
        result -= value
print(result)
    