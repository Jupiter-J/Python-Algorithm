


n = int(input())                    # _ 변수없이 돌리고 싶을 때
a=[list(map(int, input().split())) for _ in range(n)] #한줄을 읽어어서 리스트화
largest = -2147000000 #최댓값을 구함으로 초기값은 가장 작은값으로 초기화 시킨다

#행열 구하기
for i in range(n): #n만큼 행이 돈다
    sum1=sum2=0 #0으로 초기화 했기때문에 항상 0부터 합한다
    for j in range(n):
        sum1 += a[i][j] #행 탐색 (i고정 j회전)
        sum2 += a[j][i] #열 탐색 (j회전 i고정)
    if sum1>largest:
        largest = sum1 #가장 큰값
    if sum2>largest:
        largest = sum2 #가장 큰값    
#대각선 구하기
sum1=sum2=0
for i in range(n):
    sum1 +=a[i][i]
    sum2 +=a[i][n-i-1] #번째이기 때문에-1
if sum1>largest:
    largest = sum1 #가장 큰값
if sum2>largest:
    largest = sum2 #가장 큰값    
print(largest)




