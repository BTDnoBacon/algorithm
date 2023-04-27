import sys
input = sys.stdin.readline

N = int(input())
case = sorted(list(map(int, input().split())))
result = 0

for i in range(N):
    s = 0
    e = N-2
    dummy = case[:i] + case[i+1:]
    while s < e:
        if dummy[s] + dummy[e] == case[i]:
            result += 1
            break
        elif dummy[s] + dummy[e] > case[i]:
            e -= 1
        elif dummy[s] + dummy[e] < case[i]:
            s += 1


print(result)
