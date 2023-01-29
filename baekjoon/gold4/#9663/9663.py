import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N = int(input())

# count = 0
# location = []
def loca_check(cur_loca):
    for i in range(cur_loca):
        if location[i] == location[cur_loca] or abs(location[i] - location[cur_loca]) == cur_loca - i:
            return False
    return True

def backtracking(cur_loca):
    global count
    # print(cur_loca)
    if cur_loca == N:
        count += 1
    else:
        for k in range(N):
            location[cur_loca] = k
            # print('a')
            # print(location)
            if loca_check(cur_loca):
                backtracking(cur_loca + 1)
    
    # return print('b')

count = 0
location = [0 for _ in range(N)]
backtracking(0)

print(count)
