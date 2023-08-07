
"""
이분 검색
8 32
23 87 65 12 57 32 99 81
"""
n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
lt = 0
rt = len(arr)-1

while lt<=rt: #중요!
    mid = (lt+rt)// 2
    if arr[mid]==m:
        print(mid+1)
        break
    elif arr[mid]<m:
        lt=mid+1
    else:
        rt=mid-1