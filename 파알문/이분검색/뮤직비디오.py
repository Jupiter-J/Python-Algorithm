"""
뮤직비디오
9 9
1 2 3 4 5 6 7 8 9
"""

def Count(capacity):
    cnt=1
    sum=0
    for x in music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

n, m = map(int, input().split())
music = list(map(int, input().split()))
maxx = max(music)
lt=1
rt=sum(music)
answer=0
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        answer=mid
        rt=mid-1
    else:
        lt=mid+1
print(answer)