
# 입력: n명의 학생과 n명 만큼의 list받기
# 평균 구하기
# for문으로 idx=학생번호, x=성적
# tmp변수를 만들어 평균과 실제학생의 값을 구함 abs() 절댓값
# 평균거리값이 가장 작은 학생이 정답

n = int(input())
a = list(map(int, input().split()))
ave=round(sum(a)/n)
ave=ave+0.5
ave=int(ave)
min=2147000000 #최댓값을 설정해 첫째값이 들어오도록 함
for idx, x in enumerate(a): # a리스트를 탐색할때 idex, x값을 쌍으로 가져올 수 있음
     tmp=abs(x-ave) #절댓값 abs()
     if tmp<min:
        min=tmp
        score=x #성적 저장
        res=idx+1 #번째를 구하기 때문에 +1
     elif tmp == min: #같은 거리일 경우
        if x>score: #저장된 값
            score=x
            res=idx+1
print(ave, res)