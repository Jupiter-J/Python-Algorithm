
n = int(input())
a=[list(map(int, input().split())) for _ in range (n)]
res=0
s=e=n//2 #중간값을 구함
for i in range(n): 
    for j in range(s, e+1): #s~e까지기 때문에 e+1
        res += a[i][j]
    if i<n//2: #행인 i가 중간 값보다 작으면 넓히고 
        s-=1
        e+=1
    else:     #행인 i가 중간 값보다 커지면 좁힌다
        s+=1
        e-=1
print(res)
