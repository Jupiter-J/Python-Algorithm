"""
4. 두 리스트 합치기
포인트 변수가 필요 - 시간 복잡도 주의
append() : 배열 가장 끝에 요소를 추가한다
c = [] : 빈 리스트
p1이나 p2가 n 혹은 m까지 모두 처리하면 중지 = while
슬라이스 더하기 = c=c+a[p1:]
"""

# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))
#
# c = []
# p1=p2= 0
#
# while p1<n and p2<m:
#     if a[p1]<=b[p2]:
#         c.append(a[p1])
#         p1+=1
#     else:
#         c.append(b[p2])
#         p2+=1
#
# # 나머지 값 넣기
# if p1<n:
#     c=c+a[p1:]
# if p2<m:
#     c=c+b[p2:]
#
# for x in c:
#     print(x, end=' ')


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1=p2=0
c=[]
while p1<n and p2<m:
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]
for x in c:
    print(x, end=' ')
