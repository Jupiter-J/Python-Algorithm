#elif는 참위되어도 밑으로 내려가지 않는다 -> 다른 조건을 수행하지 못함

n = int(input())
res=0

for i in range(n):
    tmp = input().split() #한줄씩 띄어서 입력된다 
    tmp.sort() #오름차순 정렬
    a, b, c =map(int, tmp) #문자열을 숫자화로 변경
    
    if a==b and b==c: #가장 좋은것을 먼저 넣어야 한다(전체가 충족되는것)
        money= 10000+a*1000
    elif a==b or a==c:
        money= 1000+(a*100)
    elif b==c:
        money= 1000+(b*100)
    else:
        money= c*100
    if money>res:
        res=money
print(res)
