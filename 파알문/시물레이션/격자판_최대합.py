
"""
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

"""


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
largest= -2147000000

# 행, 열의 합
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1 += graph[i][j]
        sum2 += graph[j][i]
    if sum1 >largest:
        largest=sum1
    if sum2 > largest:
        largest=sum2

sum1=sum2=0
# 대각선 합
for i in range(n):
    sum1 += graph[i][i]
    sum2 += graph[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2


print(largest)


