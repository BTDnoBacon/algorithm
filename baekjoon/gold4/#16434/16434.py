import sys
input = sys.stdin.readline

N, H_ATK = map(int, input().split())
case = [list(map(int, input().split())) for _ in range(N)]

s = 1
e = 999999000001

while s < e:
    mid = (s+e) // 2
    MAX_HP = mid
    CUR_HP = MAX_HP
    CUR_ATK = H_ATK
    for i in range(N):
        t, a, h = case[i]
        if t == 1:
            CUR_HP -= a * (h//CUR_ATK)
        else:
            CUR_ATK += a
            CUR_HP = min(MAX_HP, CUR_HP + h)
        if CUR_HP < 1:
            break
    if CUR_HP < 1:
        s = mid + 1
    else:
        e = mid - 1

print(mid + 1)

