# K번째 약수중 n번째 작은 값 입력하기

# 1. 두 가지 값 입력받기
#값을 입력받을때 옆의로 띄어쓰기하여 받을경우 map을 사용한다 (6 3)
#숫자형으로 변환, 띄어쓰기하여 받기때문에 split -> 띄어쓰기를 구분하여 입력받는다
n , k = map(int , input().split())

# 2. 구하기
cnt=0
for i in range(1, n+1): #range(시작숫자, 종료숫자) 시작숫자부터 종료숫자 바로 앞까지 만 함으로 +1
    if n%i==0:
        cnt +=1 #나머지가 0이면 약수임으로 +1
    if cnt==k:  #k번째를 출력하기
        print(i)
        break
else:   #for-else 정상적으로 끝나면 else를 실행
    print(-1)
