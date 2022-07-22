
n = int(input())
a = list(map(int, input().split()))

# 평균구하기 - round
ave = round(sum(a)/n)
min=2147000000

# 전체 탐색 idx=학생id{인덱스}, x=값
for idx, x in enumerate(a):
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1 
    elif tmp == min:
        if x>score:
            res=idx+1