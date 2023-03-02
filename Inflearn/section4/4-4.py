
"""
첫번째 좌표에는 바로 배정하기

"""
n, c = map(int, input().split())
List=[]

def Count(len):
    cnt=1
    ep=List[0]
    for i in range(1, n):
        if List[i]-ep >= len:
            cnt+=1
            ep=List[i]
    return cnt

for i in range(n):
    tmp=int(input())
    List.append(tmp)
List.sort()
lt=1
rt=List[n-1]

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)