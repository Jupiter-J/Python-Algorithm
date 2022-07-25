

#뒤집는 함수
def reverse(x): 
    res=0 #초기화
    while x>0: 
        t= x%10 #x의 일의자리를 t로 변경
        res= res*10+t
        x=x//10 #10으로 나눈 몫
    return res 

#소수판별 함수
def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1):
        if x%i==0:
            return False
    else:
        return True

n = int(input())
a =list(map(int, input().split()))
for x in a:
    tmp = reverse(x) #뒤집어진 수를 tmp에 저장
    if isPrime(tmp):
        print(tmp, end=' ')
