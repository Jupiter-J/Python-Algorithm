
# 반복문 (for, while)
 #range(a,b) a~b까지, range(c) 0~c까지
a=range(11) 
print(list(a))

# 양수 반복문
for i in range(10): 
    print(i)

# 음수 반복문 (값이 점점 작아지게)
for j in range(10,0,-1):
    print(j)

# while 반복문
k=1
while k<=10:
    print(k)
    k=k+1

# 음수 while문
t=10
while t>=1:
    print(t)
    t=t-1


## break(특정조건일때 멈춘다)
# 무한 증가를 했다가 10일 경우 멈춘다 
m=2
while True:
    print(m)
    if m==10:
        break
    m+=1

## Continue (특정조건에서 건너뛰고 싶다)
for n in range(1,11):
    if i%2==0: # true일경우 계속 지나감. 짝수일경우 계속 지나간다
        continue
    print(n) # 홀수만 출력된다 


## for - else 구문
for t in range (1,11):
    print(t)
    if t>15:
        break #조건에 부합되면 break 후 else는 그냥 건너뜀
else:
    print(11) #break를 당하면 else는 건너뛴다. 반대로 break 다하지 않으면 출력된다