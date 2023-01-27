import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
# print(list(map(int, input().split())))

no_listen_people = set()
no_seen_people = set()

for _ in range(N):
    no_listen_people.add(input().rstrip())

for _ in range(M):
    no_seen_people.add(input().rstrip())

no_lis_seen = set()

no_lis_seen = set.intersection(no_listen_people, no_seen_people)

print(len(no_lis_seen))

temp = list(no_lis_seen)
temp.sort()

for item in temp:
    print(item)