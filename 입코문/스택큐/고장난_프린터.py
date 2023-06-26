

from collections import deque
def solution(nums):
    answer=0
    q = deque(nums)

    while q: #빈자료구조 = F/ 안에 있을경우 T
        for _ in range(2):
            if len(q) >=2:
                q.popleft()
        q.append(q.popleft())
        if len(q)==1:
            return q[0]


print(solution([3, 1, 4, 5, 2, 6, 7]))
# print(solution([10, 8, 3, 1, 4, 5, 2, 6, 7, 9]))
# print(solution([10, 8, 3, 11, 12, 1, 4, 5, 2, 6, 7, 9]))
# print(solution([10, 8, 3, 1, 4, 5, 2, 11, 13, 6, 7, 12, 9, 14]))
# print(solution([1, 8, 6, 10, 4, 7, 2, 5, 3, 9]))