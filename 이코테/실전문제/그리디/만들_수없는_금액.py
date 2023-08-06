
"""
5
3 2 1 1 9
"""

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    # target >= x
    target +=x
print(target)



# n = int(input())
# money = list(map(int, input().split()))
# money.sort()
# answer = 0
# ch = [0]*(money[-1]+1)
# ch[0]=1
#
# for i in range(1, len(money)+1):
#     t1 = t2 = 0
#     snum = 0
#     snum += money[t2]
#     t2+=1
#     while t1 < t2:
#         if snum==i:
#             ch[i]=1
#             t1=t2=0
#         else:
#             if snum >i:
#                 t1+=1
#                 snum-=money[t1]
#             else:
#                 t2+=1
#                 snum+=money[t2]
#         if t1 ==t2:
#             print(i)
#             break
#     break







