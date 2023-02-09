import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


S = list(input().rstrip())
q = int(input())
# case = [0 for _ in range(len(S)+1)]
for j in range(q):
    s,l,r = input().split()
    # if j == 0:
    #     for i in range(len(S)):
    #         if S[i] == s:
    #             case[i+1] += 1
        
    #     for i in range(2, len(S)+1):
    #         case[i] += case[i-1]
    print(S[int(l):int(r)+1].count(s))
    
    # print(case)
    # print(case[int(r)+1] - case[int(l)])