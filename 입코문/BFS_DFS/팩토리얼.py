

# def solution(n):
#     answer=1
#     for i in range(1, n+1):
#         answer *= i
#     return answer
# print(solution(5))

"""
DFS 방식
"""

def DFS(n):
    if n==1:
        return 1
    else:
        return n * DFS(n-1)
print(DFS(5))
