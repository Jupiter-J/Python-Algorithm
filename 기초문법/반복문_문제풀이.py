
# 1부터 N까지 출력
n = int(input())
for i in range(1, n+1):
    print(i)

# 1부터 N까지 홀수 출력하기
m = int(input())
for j in range(1, n+1):
    if j%2==1:
        print(j)


# 1부터 N까지 합 구하기
k = int(input())
sum=0
for k in range(1, k+1):
    sum=sum+k
print(sum)


# N의 약수 출력하기
t = int(input())
for t in range(1, t+1):
    if t%i==0: #t를 i로 나눠서 나눠 떨어지는 수가 약수
        print(t, end=' ')