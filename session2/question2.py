# 1. 테스트 케이스 입력받 T
# 2. 테스트 케이스만큼 돌리면서 n, s, e, k 입력받기
# 3. n개만큼의 리스트 입력받기

T = int(input()) #입력받으면 문자열이기 때문에 int변환
for t in range(T): #케이스별로 입력받기
    n, s, e, k = map(int, input().split())
    a= list(map(int, input().split()))
    a=a[s-1:e] # s~e번째 = [s-1:e]idx
    a.sort() #오름차순 정렬
    print("#%d %d" %(t+1, a[k-1])) # k번째 = [k-1]idx
    
