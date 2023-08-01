
"""
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

"""

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
""" 이차원 배열 생성 코드 : 비효율적임
graph=[]
for _ in range(n):
    a = list(map(int, input().split()))
    graph.append(a)
"""
graph = [list(map(int, input().split())) for _ in range(n)]

max_num = -2147000000
# 행,열 합 비교
for i in range(n):
    sum1=sum2=0 #초기화
    for j in range(n):
        sum1+=graph[i][j]
        sum2+=graph[j][i]
    if sum1>max_num:
        max_num=sum1
    if sum2>max_num:
        max_num=sum2
sum1=sum2=0

# 대각선 합 비교
for i in range(n):
    sum1+=graph[i][i]
    sum2+=graph[i][n-i-1]
if sum1>max_num:
    max_num=sum1
if sum2>max_num:
    max_num=sum2
print(max_num)
