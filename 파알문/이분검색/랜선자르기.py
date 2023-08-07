
"""
4 11
802
743
457
539
"""

def Count(len):
    cnt=0
    for x in arr: #전체 랜선 갯수 구하기
        cnt+=(x//len)
    return cnt

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
arr.sort(reverse=True)

lt=1
rt=arr[0]

while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid)>=n:
        answer=mid
        lt=mid+1 #랜선의 최대길이를 구해야함으로 lt를 늘린다
    else:
        rt=mid-1

print(answer)


