import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, P = map(int, input().split())

melody = [0 for _ in range(N+1)]
count = 0

for _ in range(N):
    note, fret = map(int, input().split())
    if melody[note] == 0:
        melody[note] = []

    while melody[note]:
        if melody[note][-1] < fret:
            melody[note].append(fret)
            count += 1
            break
        elif melody[note][-1] == fret:
            break
        else:
            count += 1
            melody[note].pop()
    
    if len(melody[note]) == 0:
        melody[note].append(fret)
        count += 1

print(count)
    
