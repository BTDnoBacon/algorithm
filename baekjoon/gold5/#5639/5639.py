import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline




def postorder(n):
    
    if 2*n < len(case):
        postorder(2*n)
        postorder(2*n + 1)
    print(case[n])



temp = []
case = [0]
while True:
    try:
        case.append(int(input()))
    except:
        break

postorder(1)