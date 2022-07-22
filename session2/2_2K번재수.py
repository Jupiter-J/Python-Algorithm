
#1. 테스트 케이스 t를 입력받기 + 정수화
t = int(input())
#2. 케이스만큼 회전시킨다
for t in range(t):
#3. 각 케이스별로 읽어들인다 (띄어쓰기 된것을 하나씩 받는 방법은?)
    n, s, e, k = map(int, input().split())
#4. 리스트에 저장해서 map으로 읽은값을 저장 
    a= list(map(int, input().split()))
#5. 저장한 값에서 오름차순 정렬
    a=a[s-1:e] 
#6. 오름차순이 된 값을 출력
    a.sort()
#7. 0번부터 돌기때문에 +1
    print("#%d %d" %(t+1,a[k-1]))
