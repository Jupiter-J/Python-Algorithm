
"""
스택
( - 무조건 스택에 넣기
) - 앞의것이 (일 경우
"""

s=input()
stack=[]
cnt=0 # 쇠막대기 조각 누적


for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i]) #여는 괄호일 경우 집어넣기
    else:
        stack.pop()
        if s[i-1]=='(': #닫는 괄호일경우, 바로 앞의 지점이 여는괄호인지 확인 - 레이저 확인유무
            cnt+=len(stack) #길이를 누적시킨다
        else:
            cnt+=1
