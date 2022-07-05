'''
두개의 주사위를 던져서 나올 수 있는 눈의 합중 가장 
확률이 높은 숫자를 출력하는 프로그램
'''

# 값을 입력받는다
n, m = map(int, input().split())
# cnt 갯수 = 나온 눈의 합 더하기 +3(여유분)
cnt=[0]*(n+m+3) 
max= -214700000 #가장 작은 값으로 초기화

# 주사위 2개를 던졌을 경우 경우의 수
    # n+1: n전까지만 돌기 때문에 +1
for i in range(1, n+1): 
    for j in range(1, m+1):
        #cnt는 i+j의 값이 인덱스이며 같은값이 나오면 +1을 한다.  
        cnt[i+j] +=1

# cnt리스트에서 빈도 횟수의 최댓값 찾기
for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]

# 최댓값의 인덱스 출력하기 
for i in range(n+m+1):
        #구해진 최댓값들의 cnt[i]를 출력해야함
        #cnt 인덱스가 곧 합을 의미함 
    if cnt[i]==max:
        print(i, end=' ')
