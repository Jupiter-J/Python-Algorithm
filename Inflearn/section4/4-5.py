

"""
그리디 알고리즘
현재 상황에서 지금 당장 좋은 것만 고르는 방법

회의실배정
회의가 끝나는 시간을 기준으로 해야함 (빨리끝나는게 중요)
끝수가 크거나 같을 경우 사용

# 끝나는 시간을 기준으로 정렬 하는 방법
meeting.sort(key=lambda x: (x[1], x[0]))

"""

# n = int(input())
# meeting=[]
#
# for i in range(n):
#     s, e = map(int, input().split())
#     meeting.append((s,e)) #튜플로 집어 넣는다
# meeting.sort(key=lambda x: (x[1], x[0]))
#
# et=0
# cnt=0
# #meeting 리스트가 인덱스, 값 같은 한쌍으로 이루어져있기 때문에 변수 두개를 사용 s,e
# for s, e in meeting:
#     if s>=et:
#         et=e
#         cnt+=1
# print(cnt)

n = int(input())
meeting=[]

for i in range(n):
    s,e = map(int, input().split())
    meeting.append((s,e))
meeting.sort(key=lambda x: (x[1],x[0]))

end=0
cnt=0
for s,e in meeting:
    if s >= end:
        end=e
        cnt+=1
print(cnt)
