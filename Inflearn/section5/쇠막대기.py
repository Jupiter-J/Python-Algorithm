
"""
쇠막대기
"""

# arr = input()
# stack=[]
# cnt=0
#
# for i in range(len(arr)):
#     if arr[i]=='(':
#         stack.append(arr[i])
#     else:
#         stack.pop()
#         if arr[i-1]=='(': #쇠막대기 ******
#             cnt+=len(stack)
#         else:
#             cnt+=1
# print(cnt)



n = input()
cnt=0
stack=[]
for i in range(len(n)):
    if n[i]=='(':
        stack.append(n[i])
    else:
        stack.pop()
        if n[i-1]=='(':
            cnt+=len(stack)
        else:
            cnt+=1

