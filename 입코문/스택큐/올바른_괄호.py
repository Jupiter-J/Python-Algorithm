

"""
스택문제

# ) 닫는 괄호가 더 많을 경우 -> stack이 비어있을 수 있다
# (()) )( -> 닫는 괄호가 만났을때 스택이 비어서 True로 오인할 수 있음
"""

def solution(s):
    answer= "YES"
    stack=[]
    for x in s:
        if x == ')': #닫는괄호 기준
            if len(stack)==0: #순서가 바꼈거나, 닫는괄호가 많은 경우
                return "NO"
            stack.pop()
        else:
            stack.append(x)
    if len(stack)>0: #스택이 남아있을경우 - 여는괄호가 많은 경우
        return "NO"
    return answer

print(solution("((()))()"))
# print(solution("(()(()"))
# print(solution("()())"))
# print(solution("())("))
# print(solution("((())))()("))
