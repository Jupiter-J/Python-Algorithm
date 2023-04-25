

"""
대표값
round() : 반올림
enumerate() : 인덱스번호 쌍 대응하는 리스트
"""

# n = int(input())
# a = list(map(int, input().split()))
# ave= round(sum(a)/n)
# min=2147000000
#
# for idx, x in enumerate(a):
#     tmp=abs(x-ave)
#     if tmp<min: #절대값의 최솟값을 찾기
#         min=tmp
#         score=x #점수
#         res=idx+1 #학생번호
#     elif tmp==min: #최솟값이 같을때
#         if x> score:# 점수가 큰쪽이 답이됨
#             score=x
#             res=idx+1
#
# print(ave, res)


n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n)
min = 2147000000

for idx, x in enumerate(a):
    tmp= abs(x-ave)
    if tmp<min:
        score=x
        stid=idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1
            
print(ave,res)


