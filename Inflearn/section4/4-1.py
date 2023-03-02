"""
m=출력하고자 하는 번째
이분검색:: 중간을 나눠서 원하는 값 보다 크고작음을 확인후 반절을 없앨 수 있다
log(n)
"""

# n, m = map(int, input().split())
# a = list(map(int, input().split()))
#
# # 오름차순
# a.sort()
#
# # 이분검색
# lt=0
# rt=n-1
# while lt <= rt:
#     mid=(lt+rt)//2
#     if a[mid]==m:
#         print(mid+1)
#         break
#     elif a[mid]>m:
#         rt=mid-1
#     else:
#         lt=mid+1

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
lt=0
rt=n-1

while lt <= rt:
    mid=(lt+rt)//2
    if a[mid]== m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt=mid-1
    else:
        lt=mid+1
