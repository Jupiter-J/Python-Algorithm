
"""
5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20
"""
# change = []
# card = [i for i in range(1,21)]
# for i in range(10):
#     a, b = map(int, input().split())
#     change.append([a,b])
#
# for a, b in change:
#     n = (b-a)//2+1
#     while n>0:
#         card[a-1], card[b-1] = card[b-1], card[a-1]
#         n -= 1
#         a+=1
#         b-=1




a = list(range(21)) # 더 간단하게 생성
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i],a[e-i]=a[e-i],a[s+i]

a.pop(0)
for x in a:
    print(x, end=' ')
