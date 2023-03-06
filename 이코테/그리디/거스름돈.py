
"""
큰 단위부터 돈을 거슬러 준다
"""

n = int(input())
cnt = 0
coin=[500,100,50,10]

for x in coin:
    cnt += n//x
    n %= x

print(cnt)