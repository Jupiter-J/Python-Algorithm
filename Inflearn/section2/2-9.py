"""
if - elif는 가장 먼저 참이 되면 그대로 빠져나온다

"""

n = int(input())
res=0

for i in range(n):
    tmp=input().split()
    tmp.sort()
    a, b, c = map(int, tmp) #리스트를 숫자화
    if a==b and b==c:
        money=10000+a*1000
    elif a==b or a==c:
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money=c*100
    if money>res:
        res=money
print(res)