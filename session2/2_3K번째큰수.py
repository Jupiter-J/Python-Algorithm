# 중복일 경우 한번만 카운트 한다

#1. 입력받는다 
n, k = map(int, input().split())
a = list(map(int, input().split())) # n개의 자료를 입력받는 경우

#2. 중복값 없애기 - set()
res=set()
#3. 0부터 n 전까지 돈다 
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i] + a[j] + a[m])
res=list(res)
res.sort(reverse=True)
print(res[k-1])

