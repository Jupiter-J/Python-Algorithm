

#1. 입력값 : n, k받기
n = int(input())
a= list(map(int, input().split())) 

'''
2. 평균값 구하기
     - 반올림을 할것 round(): round_half_even 짝수쪽으로 기울어짐
        a=a+0.5
        a=int(a)
     - 전체 더하기 sum()
     - 나누기 (평균)
'''
ave = sum(a)/n
ave = ave+0.5
ave = int(ave)

'''
enumberate : idx와 원소를 동시에 접근하면 루프를 돌리는 방법
인덱스와 값을 객체형태로 리턴해준다 
'''
min=2147000000
for idx, x in enumerate(a):
#3. 평균과 학생의 실제 거리 구하기
# abs() : 절댓값을 반환하는 함수
# tmp 값이 가장 작은 원소가 가까운 거리라는 의미
    tmp=abs(x-ave)
    if tmp<min:
        min = tmp #최솟값 저장
        score=x #점수값 저장
        res=idx+1 #인덱스는 0부터 시작하기 때문에 +1
    elif tmp == min: #같은 거리가 나올경우
        if x>score:
            score= x
            res=idx+1
print(ave, res)