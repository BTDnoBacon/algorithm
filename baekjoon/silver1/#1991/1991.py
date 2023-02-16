import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(node_dict[node][0])
        preorder(node_dict[node][1])

def inorder(node):
    if node != '.':
        inorder(node_dict[node][0])
        print(node, end='')
        inorder(node_dict[node][1])

def postorder(node):
    if node != '.':
        postorder(node_dict[node][0])
        postorder(node_dict[node][1])
        print(node, end='')

N = int(input())
node_dict = dict()

for _ in range(N):
    node, left, right = input().split()
    node_dict[node] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
