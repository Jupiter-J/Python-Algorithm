
n, m=map(int, input().split())
a=list(map(int, input().split()))
lt=0 #lt는 무조건 rt보다 작거나 같다
rt=1
tot=a[0] #1t~ rt앞까지의 합이다
cnt=0

while True:
    if tot<m: #1. m보다 작을때
        if rt<n: #rt가 먼저 도달하기 때문에 n에 닿을때 끝난다 
            tot += a[rt]
            rt +=1
        else:
            break #n보다 크면 멈춤
    elif tot ==m: #2. m과 같을때
        cnt +=1
        tot -=a[lt]
        lt +=1
    else: #3. m보다 클때
        tot -=a[lt]
        lt +=1
print(cnt)

