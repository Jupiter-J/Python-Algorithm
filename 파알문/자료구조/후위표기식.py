
"""
3+5*2/(7-2)
"""
s = input()
stack = []
answer = ""
for x in s:
    if x.isdigit():
        answer+=x
    else:
        if x=='(':
            stack.append(x)
        elif x=="*" or x=="/":
            while stack and (stack[-1]=='*' or stack[-1]=='/'): #스택을 돌면서 연산자 우선순위 확인
                answer +=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(': #순위가 가장 밑이기 때문에 다 출력 but (여는 괄호 전까지
                answer+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                answer+=stack.pop()
            stack.pop()
while stack:
    answer+=stack.pop()

print(answer)





