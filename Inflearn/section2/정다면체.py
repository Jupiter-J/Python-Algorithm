

# n, m = map(int, input().split())
# cnt=[0]*(n+m+3)
# max= -2147000000
# tmp=0
#
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         cnt[i+j]+=1
#
# for k in range(n+m+1):
#     if cnt[k]>max:
#         max=cnt[k]
#
# for i in range(n+m+1):
#     if cnt[i]==max:
#         print(i, end=' ')

"""
정다면체
리스트활용문제
"""


n, m = map(int, input().split())
cnt = [0]*(n+m+3)
max= -2147000000

# 전체 경우의 수 구하기
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j]+=1

# 최대 확률 구하기
for i in range(n+m+1):
    if cnt[i]> max:
        max=cnt[i]
# 최대 확률 출력
for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ')