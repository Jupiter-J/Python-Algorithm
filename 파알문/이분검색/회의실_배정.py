
"""
5
1 4
2 3
3 5
4 6
5 7
"""

# [[1, 4], [2, 3], [3, 5], [4, 6], [5, 7]]
n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]

# 어떤 기준으로 정렬을 해야할까? [[2, 3], [1, 4], [3, 5], [4, 6], [5, 7]]
arr.sort(key=lambda v:v[1])

next=0
answer=0
for start, end in arr:
    if start>=next: #다음 시작시간 >= 현재 끝나는 시간 (최초값은 0임으로 자동 시작)
        next=end
        answer+=1
print(answer)