

"""
그리디
회의가 끝나는 시간을 기준으로 정렬

"""

n = int(input())
meeting=[]
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s,e))
for x in meeting:
    print(x)
