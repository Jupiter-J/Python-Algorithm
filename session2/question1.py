
#1. 두개의 값을 입력 N, K
n, k= map(int, input().split())
#2. 입력받은 값만큼 돌려서 나눠 약수를 구한다
cnt =0
for i in range(1, n+1): #약수는 1부터 존재 
    if n%i==0: # 나머지가 0이면 약수
        cnt += 1
    if cnt == k:
        print(i)
        break
else: #정상적으로 끝날경우
     print(-1)