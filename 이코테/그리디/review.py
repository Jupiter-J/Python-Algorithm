
"""
큰수의 법칙
5 8 3
2 4 5 4 6
"""

n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort(reverse=True)
answer=0

while True:
    for i in range(k):
        if m==0:
            break
        answer += num[0]
        m-=1
    if m==0:
        break
    answer += num[1]
    m-=1

print(answer)