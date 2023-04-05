
"""
시간초과 뜸
"""
# n, m = map(int, input().split())
# num =list(map(int, input().split()))
#
# for k in range(m):
#     i, j = map(int, input().split())
#     new = num[i-1:j]
#     print(sum(new))

"""
새 코드
합배열 숙지 , import sys 사용시 시간단축 가능 
input = sys.stdin.readline
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num =list(map(int, input().split()))
# 합 배열 생성
new=[0]
temp=0

for i in num:
    temp += i
    new.append(temp)

for i in range(m):
    s, e = map(int, input().split())
    print(new[e]-new[s-1])