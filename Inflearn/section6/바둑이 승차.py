
"""
바둑이 승차
"""

# c, n = map(int, input().split())
# a = []
#
# for i in range(n):
#     tmp = int(input())
#     a.append(tmp)
#
# a.sort()
# print(sum(a)-a[0])

# def DFS(L, sum, tsum):
#     global result
#     if sum+(total-tsum)<result:
#         return
#     if sum>c:
#         return
#     if L==n:
#         if sum>result:
#             result=sum
#     else:
#         DFS(L+1, sum+a[L], tsum+a[L])
#         DFS(L+1, sum)
#
# c, n = map(int, input().split())
# a = [0]*n
# result=-21747000000
# for i in range(n):
#     a[i]=int(input())
#     total=sum(a)
#     DFS(0,0,0)
# print(result)

#L=인덱스 번호, sum=부분집합의 합
def DFS(L, sum):
    global result
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

c, n = map(int, input().split())
a=[0]*n #바둑이 무게 저장
result=-2147000000 #가장큰값을 구하기 위해
for i in range(n):
    a[i]=int(input())
DFS(0,0)
print(result)