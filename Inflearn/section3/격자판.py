
"""
격자판
1. 한줄을 읽고 리스트화 = [list(map(int,input().split()))]
2. N열을 읽고 한줄씩 리스트화 = [list(map(int,input().split())) for _ in range(n)]

5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

"""



# # # 입력 받는 법
# n = int(input())
# a = [list(map(int,input().split())) for _ in range(n)]
#
# largest= -2147000000
# for i in range(n):
#     sum1=sum2=0
#     for j in range(n):
#         sum1+= a[i][j] #행 고정
#         sum2+= a[j][i] #열 고정
#     if sum1>largest:
#         largest=sum1
#     if sum2>largest:
#         largest=sum2
# sum1=sum2=0
# for i in range(n):
#     sum1+=a[i][i]
#     sum2+=a[i][n-i-1]
# if sum1>largest:
#     largest=sum1
# if sum2>largest:
#     largest=sum2
# print(largest)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 행의 합
# 열의 합
largest = -2147000000

for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j] #행의합
        sum2+=a[j][i] #열의합
    if sum1> largest:
        largest=sum1
    if sum2> largest:
        largest=sum2
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
if sum1>largest:
    largest=sum1
if sum2>largest:
    largest=sum2
print(largest)

