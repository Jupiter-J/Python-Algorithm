
"""
이분검색
lt, rt 변수를 사용해서 절반씩 좁혀나가는 방식
이진탐색 = 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
"""


# n, m = map(int, input().split())
# n_list = list(map(int, input().split()))
# n_list.sort()

# 순차탐색
# cnt=0
# for i in n_list:
#     cnt+=1
#     if m==i:
#         print(cnt)


# # 이진탐색
# lt=0
# rt=n-1
# while lt<=rt:
#     mid=(lt+rt)//2
#     if n_list[mid]==m:
#         print(mid+1)
#         break
#     elif n_list[mid]>m:
#         rt=mid-1
#     else:
#         lt=mid+1

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt=0
rt=n-1

while lt<=rt:
    mid=(lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid+1
    else:
        lt=mid+1
