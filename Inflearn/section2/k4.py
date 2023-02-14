
"""
최솟값 구하기
- 가장 작은 값으로 초기화
"""
# arr=[5,3,7,9,2,5,2,6]
# arrMin=float('inf')
# for i in range(len(arr)):
#     if arr[i]<arrMin:
#         arrMin=arr[i]
# print(arrMin)
#
# for x in arr:
#     if x < arrMin:
#         arrMin=x
# print(arrMin)

"""
4. 대표값
평균 구하기 - 반올림
- 소수 정수화 : round() 소수 첫째 자리에서 반올림
- 리스트의 합 : sum()
- 리스트 인덱스 값 반환 : enumerate()
    리스트 (인덱스 값, 실제값)쌍으로 대응하여 탐색
- 절대값 : abs()    
"""

# N=int(input())
# score=list(map(int,input().split()))
# avg=round(sum(score)/N)
# min=2147000000
#
# for idx, x in enumerate(score):
#     tmp=abs(x-avg)
#     if tmp<min:
#         min=tmp
#         result=x  # min:크기 / result=실제값 저장
#         res=idx+1 # res: (학생번호)+1
#     elif tmp==min: # elif = else if : 같은 값일 경우(차이가 똑같을 경우)
#         if x>result: # 현재 학생의 점수 x > 저장된 값
#             result=x
#             res=idx+1
# print(avg,res)

n= int(input())
score = list(map(int, input().split()))
avg = round(sum(score)/n)
min = 2147000000

for idx, x in enumerate(score):
    a = abs(x-avg)
    if a < min:
        min = a
        stuNum = idx+1
        result = x
    elif a == min:
        if x > result:
            stuNum = idx +1
            result = x

print(avg, stuNum)





