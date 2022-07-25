
# cnt라는 리스트에 경우의수로 나온 합의 값들을 인덱스에 저장 한다
# cnt 리스트의 인덱스 번호가 나온 합이고 같은 값이 나올때마다 count증가
# 확률이 높다 = 인덱스 번호에 count가 높은것 

n, m =map(int, input().split())
cnt=[0]*(n+m+3) #정다면체 두개의 합 이상의 값이 나올리가 없음
max=-214700000 #max는 가장 작은값으로 초기화

for i in range(1, n+1): #n번째 까지 임으로 n+1
    for j in range(1, m+1): #주사위는 중복이 나올 수 있고 카운트 해야함
        cnt[i+j]+=1 #주사위 눈의 합 == idx
for i in range(n+m+1): #두 눈의 합이 최대 idx이며 ~까지라 +1
    if cnt[i]>max: #cnt[i = 합]이고 이것의 값이 확률, 값인 확률을 비교하여 max에 저장
        max=cnt[i] 
for i in range(n+m+1):
    if cnt[i]==max: #i가 출력되도록 해야함  
        print(i, end=' ')