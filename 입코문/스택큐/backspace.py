

"""
Backspace
"""
from collections import deque
def solution(s):
    stack = deque()
    for x in s:
        if x=="#":
            if len(stack)>0: #이 먼저 나올 수 있음으로 반드시 값이 있도록 하기위해
                stack.pop()
        else:
            stack.append(x)
    return ''.join(stack)


print(solution("abc##ec#ab"))
print(solution("kefd#ef##s##"))
print(solution("teac#cher##er"))
print(solution("englitk##shabcde##ff##ef##ashe####"))
print(solution("itistime####gold"))