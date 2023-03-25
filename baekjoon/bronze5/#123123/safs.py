fn = ['2', '+', '3', '*', '4', '/', '5']
stack = [0] * len(fn)
top = -1
postfix = ''
op = {'*':2, '/':2, '+':1, '-':1}

for t in fn:
    if '0'<= t <= '9':                 # 피연산자인 경우
        postfix += t
    elif t in op:                           # 연산자인 경우
        if top == -1 or op[stack[top]] < op[t]:         # 스택이 비어있거나 토큰의 우선순위가 높으면
            top += 1                                       # push
            stack[top] = t
        else:
            while top > -1 and op[stack[top]] >= op[t]:            # 스택에 남아있고 토큰의 우선순위가 높을 때 까지
                top -= 1                                           # pop
                postfix += stack[top+1]
            top += 1  # push
            stack[top] = t
while top > -1:         # 스택에 연산자가 남아있으면
    top -= 1            # pop
    postfix += stack[top + 1]
print(postfix)