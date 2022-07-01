

# n, k를 입력받아 k번째의 약수를 구하기

#1. 값을 입력받기
n , k = map(int, input().split())

#2. 약수를 구하고 k번째 구하기
cnt =0
for i in range(1, n+1):
    if n%i == 0:
        cnt += 1
    if i == k:
        print(k)
        break
else:
    print(-1)