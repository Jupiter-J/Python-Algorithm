
# n = int(input())
# answer=0
# ch=[0]*(n+1)
# cnt=0
#
# for i in range(2, n+1):
#     if ch[i]==0:
#         cnt+=1 #소수의 갯수
#         for j in range(i, n+1, i): #참일때 배수로 회전(i부터 n+1까지, i배수만큼)
#             ch[j]=1 #걸러내기
# print(cnt)
#


"""
에라토스 테네스체
"""

n= int(input())
ch = [0]*(n+1)
cnt=0

for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1

print(cnt)
