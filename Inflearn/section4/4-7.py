
"""
최댓값, 최솟값 구하기
- 큰쪽이 가장 작은애를 나눠준다 가장 작은값이 2개 이상이 될때 까지

m을 1씩 줄여서 계산하려고 했음 (비효율적)
수직선상에 둔다고 생각하고 오름차순 정렬을 해서 앞뒤 +=해주기
"""


# L = int(input())
# a=list(map(int, input().split()))
# m = int(input())
# a.sort()
#
# for _ in range(m):
#     a[0]+=1
#     a[L-1]-=1
#     a.sort()
#
# print(a[L-1]-a[0])

L = int(input())
boxes = list(map(int, input().split()))
m = int(input())
boxes.sort()

for _ in range(m):
    boxes[0]-=1
    boxes[L-1]+=1
    boxes.sort()

print(boxes[L-1] - boxes[0])
