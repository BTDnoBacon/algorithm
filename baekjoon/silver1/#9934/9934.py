import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def inorder(li, level):
    if len(li) == 0:
        return
    
    mid = len(li)//2
    result[level].append(li[mid])
    inorder(li[:mid], level + 1)
    inorder(li[mid+1:], level + 1)
    


K = int(input())
building = list(map(int, input().split()))
# print(building)
result = [[] for _ in range(K)]
inorder(building, 0)
for item in result:
    print(*item)
