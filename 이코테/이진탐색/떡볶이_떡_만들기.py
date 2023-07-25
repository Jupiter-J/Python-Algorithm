"""
4 6
19 15 10 17
"""

n, m = map(int, input().split())
arr = list(map(int, input().split()))

lt = 0
rt = max(arr)
answer=0

while lt <=rt:
    save = 0
    mid = (lt+rt) // 2
    for x in arr:
        if x>mid:
            save += x-mid
        else:
            continue
    if save>mid: #sv 더 클경우
        lt = mid+1
        answer = mid
    else:
        rt = mid-1

print(answer)


# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
#
# lt = 0
# rt = max(arr)
# answer=0
#
# while lt <=rt:
#     save = 0
#     mid = (lt+rt) // 2
#     for x in arr:
#         if x>mid:
#             save += x-mid
#         else:
#             continue
#     if save<mid:
#         rt = mid-1
#     else:
#         answer = mid
#         lt = mid+1
# print(answer)

# # H는 M보다 같거나 크다
# arr.sort(reverse=True)
# save=0
# for h in arr:
#     for x in arr:
#         if h<x:
#             save += x-h
#         else:
#             continue
#         if save>m:


