

"""
이웃한, 짝꿍 같은 워딩이 나오면 스택 의심하기
"""

def solution(s):
    answer = ""
    stack=[]
    for x in s:
        if stack and stack[-1] == x: #스택이 비어있지 않으면, 스택 상단값
            stack.pop()
        else: #스택이 비어있음
            stack.append(x)
    return "".join(stack)

print(solution("acbbcaa"))
# print(solution("bacccaba"))
# print(solution("aabaababbaa"))
# print(solution("bcaacccbaabccabbaa"))
# print(solution("cacaabbc"))