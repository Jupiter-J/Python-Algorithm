
"""
큰 단위부터 돈을 거슬러 준다
시간복잡도 N
"""

n = int(input())
money = [500, 100, 50, 10]
cnt=0

for c in money:
    cnt+=n//c #몫 - 동전갯수
    n%=c
print(cnt)