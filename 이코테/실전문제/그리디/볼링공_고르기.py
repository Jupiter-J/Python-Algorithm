
"""
볼링공 고르기
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
"""


n, m = map(int, input().split())
data = list(map(int, input().split()))
answer=0
# 볼링공 무게 리스트
array = [0]*11

# 무게에 해당되는 볼링공 갯수 구하기
for x in data:
    array[x]+=1

"""
n5 m3
볼링공 무게 리스트 : 1 3 2 3 2
"""

# 1-m까지 무게 처리
for i in range(1, m+1):
    n-= array[i] # A선택할 수 있는 개수 제외
    answer+= array[i]*n #B가 선택하는 경우의 수, 곱하기
print(answer)


# from itertools import combinations, permutations
# n, m = map(int, input().split())
# k = list(map(int, input().split()))
#
# perm = list(combinations(k,2))
# answer=0
# for x, y in perm:
#     if x!=y:
#         answer+=1
# print(answer)

