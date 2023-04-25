
"""
주사위게임
문자로 리스트 받기 input().split()
"""

n = int(input())
res=0
for i in range(n):
    tmp= input().split() #문자화 된 리스트
    tmp.sort() #오름차순 정렬
    a, b, c = map(int, tmp) #각각의 변수에 맵핑하기
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


