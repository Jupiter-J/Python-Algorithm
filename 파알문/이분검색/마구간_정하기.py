

"""
5 3
1
2
8
4
9
"""
def Count(len):
    cnt=1
    ep=cage[0] #첫번째 마굿간에 말 배치
    for x in range(1, n):
         # 현재 내가 배치하려는 지점 - 마지막에 말을 배치한 지점
        if cage[x]-ep>=len:
            cnt+=1
            ep=cage[x]
    return cnt #배치한 말의 마릿수

n, c= map(int, input().split())
cage = [int(input()) for _ in range(n)]
cage.sort()
lt=1
rt = cage[-1]
res=0
while lt<=rt:
    mid=(lt+rt)//2 #가장 가까운 두 말의 거리
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)