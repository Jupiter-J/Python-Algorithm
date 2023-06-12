
s = "[](){}"
from collections import deque
def bracket(s):
    stack=[]
    for i in s:
        if len(stack)==0:
            stack.append(i)
        elif stack[-1] == '[' and i == ']':
            stack.pop()
        elif stack[-1] == "(" and i == ')':
            stack.pop()
        elif stack[-1] == '{' and i == '}':
            stack.pop()
        else:
            stack.append(i)
    return len(stack) == 0
def solution(s):
    answer=0
    s = deque(s)
    for i in range(len(s)):
        s.rotate(-1) #왼쪽으로 회전
        if bracket(s):
            answer +=1
    return answer

print(solution(s))