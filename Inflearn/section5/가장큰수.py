
"""
가장큰 수 - 스택
"""
# n,m = map(int, input().split())
# n = list(map(int, str(n))) #정수를 문자열 타입 리스트화 시키기
# stack=[]
#
# for i in n:
#     while stack and m>0 and stack[-1]<i: #stack비어있지 않고
#         stack.pop()
#         m-=1
#     stack.append(i)
# if m!=0:
#     stack=stack[:-m]
# res=''.join(map(str, stack)) #string을 붙인다


num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []

for i in num:
    while stack and m>0 and stack[-1]<i:
        stack.pop()
        m-=1
    stack.append(i)
if m!=0:
    stack=stack[:-m]
res=''.join(map(str, stack))
print(res)
