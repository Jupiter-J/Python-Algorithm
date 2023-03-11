
"""
응급실
"""

from collections import deque
n, m = map(int, input().split())
people = [(pos , val) for pos, val in enumerate(list(map(int, input().split())))]
# list(map(int, input().split())) = 입력받음  ex.[60,50,70]
# pos=인덱스, val=값
# 결과 ex.[(0,60),(1,50),(2,70)]

people = deque(people)
cnt=0

print(people[0]) #(0,60)

test=people[0]
print('인덱스:' ,test[0]) # 인덱스: 0
print('값:' ,test[1])  #값: 60

while True:
    cur=people.popleft()
    if any(cur[1]<x[1] for x in people): #한번이라도 T면 멈춤
        people.append(cur)
    else:
        cnt+=1
        if cur[0]==m: # m번째일때 출력
            break
print(cnt)