
"""
모험가 길드
5
2 3 1 2 2
"""

n = int(input())
traveler = list(map(int, input().split()))
traveler.sort()

answer = 0
people = 0
for x in traveler:
    people +=1
    if people >= x: # 현재 그룹에 포함된 모험가 수 >= 현재 확인 하고 있는 공포도
        answer +=1
        people = 0
print(answer)






