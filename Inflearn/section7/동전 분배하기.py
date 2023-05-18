

"""
동전분배
"""
# def DFS(L):
#   global res
#   if L==n:
#     cha=max(money)-min(money)
#     if cha<res: #최솟값, 3 개의 값이 다 달라야함
#       tmp=set()
#       for x in money:
#         tmp.add(x)
#       if len(tmp)==3: #서로다르면 3개,
#         res=cha
#   else:
#     for i in range(3):
#       money[i]+=coin[L] #누적
#       DFS(L+1)
#       money[i]-=coin[L] #취소
#
# n = int(input())
# coin=[]
# res=2147000000 #차의 최솟값
# money = [0]*3
# for _ in range(n):
#   coin.append(int(input()))
# DFS(0)
# print(res)


def DFS(L):
  global res
  if L==n:
    cha = max(money)-min(money)
    if cha <res:
      tmp=set()
      for x in money:
        tmp.add(x)
      if len(tmp)==3:
        res=cha
  else:
    for i in range(3):
      money[i]+=c[L]
      DFS(L+1)
      money[i]-=c[L]

n = int(input())
c = []
money = [0]*3
for _ in range(n):
  c.append(int(input()))
res = 2147000000
DFS(0)
print(res)