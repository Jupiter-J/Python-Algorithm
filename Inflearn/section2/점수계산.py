"""
점수계산
"""

n= int(input())
a= list(map(int, input().split()))
save=0
score=0
for i in a:
    if i==1:
        score+=1
        save+=score #누적합 구하는 방법
    else:
        score=0

print(save)


