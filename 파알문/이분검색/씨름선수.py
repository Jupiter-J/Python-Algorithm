

"""
5
172 67
183 65
180 70
170 72
181 60
"""

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]

#키 오름차순 정렬
people.sort( key=lambda v:-v[0]) #[[183, 65], [181, 60], [180, 70], [172, 67], [170, 72]]

answer=0
maxw = -2147000000
for height,weight in people:
    if weight > maxw:
        maxw = weight
        answer+=1
print(answer)