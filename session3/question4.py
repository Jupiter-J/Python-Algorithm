
'''
sort()는 n log n
n번만에 돌리기
'''

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1=p2=0 #포인트 변수 초기화
c=[] #big list
while p1<n and p2<m:#둘중 하나라도 포인트가 끝까지 도달하면 멈춤
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1 +=1
    else:
        c.append(b[p2])
        p2 +=1
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]
#원소를 하나씩 출력
for x in c:
    print(x, end=' ')