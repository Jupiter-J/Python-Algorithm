
"""
숫자만 추출
"""

# s = input()
# add=''
# for i in s:
#     if i.isdigit():
#         add+=i
# add= int(add)
# print(add)
# cnt=0
# for i in range(1, add+1):
#     if add%i==0:
#         cnt+=1
# print(cnt)

s = input()
for i in s:
    if i.isdigit():
        res=0
        res=res*10+int(i)
print(res)
cnt=0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)




