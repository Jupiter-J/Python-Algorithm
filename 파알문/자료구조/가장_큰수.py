
"""
5276823 3
"""
n, m = map(str, input().split())
#숫자 문자열을 숫자 리스트로 변환
n = list(map(int, n))
stack = []

for x in n:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
print(stack)