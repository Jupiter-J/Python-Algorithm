"""
3장이 꼭 나눠져야 답이되는게 아님
리스트 전체 합 구하기 sum(리스트 명)
"""

n, m = map(int, input().split())
Music = list(map(int, input().split()))
maxx=max(Music)

def Count(capacity):
    cnt=1
    sum=0
    for x in Music:
        if sum+x > capacity:  #누적된 시간
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

lt=1
rt=sum(Music) #리스트 전체 합
res=0
while lt <=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)


