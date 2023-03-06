
"""
씨름선수
- 가장 큰키
- 가장 무거운사람
- 큰키보다 무게가 많이 나가거나, 무거운애보다 키가 크거나

기준을 하나만 잡고 하기 - 키 기준
몸무게를 비교
"""

n = int(input())
member=[]

for i in range(n):
    h, w = map(int, input().split())
    member.append((h,w))
member.sort(reverse=True) #내림차순 정렬

cnt=0
maxValue = -217000000
for h, w in member:
    if w>maxValue:
        maxValue=w
        cnt+=1
print(cnt)