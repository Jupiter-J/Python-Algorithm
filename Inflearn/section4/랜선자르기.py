

k, n = map(int, input().split())
line=[]
res=0
largest=0

def Count(len):
    cnt=0
    for x in line:
        cnt+=(x//len)
        return cnt

for i in range(k):
    tmp=int(input()) #정수로 하나씩 받기
    line.append(tmp) #리스트 추가
    largest=max(largest, tmp) #기존값 vs 새로운값 비교

lt=1
rt=largest

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
