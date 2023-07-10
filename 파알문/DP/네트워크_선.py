
"""
네트워크 선 자르기 Bottom Up
- 점화식 : 각 항들의 관계를 나타낸 식  f(n)=f(n-1)+f(n-2)
"""

# def solution(line):
#     dy=[0]*(line+1)
#     dy[1] = 1
#     dy[2] = 2
#     for i in range(3, line+1):
#         dy[i]=dy[i-1]+dy[i-2]
#     return dy[line]

# def solution(line):
#     answer=0
#     dy=[0]*(line+1)
#     dy[1]=1
#     dy[2]=2
#     for i in range(3, line+1):
#         dy[i]=dy[i-1]+dy[i-2]
#     answer = dy[i]
#     return answer
# print(solution(7))


"""
네트워크 선 자르기 Top-Down
DFS사용
"""

def DFS(line):
    dy=[0]*(line+1)
    if dy[line]>0: # 메모리제이션 - 가지커트
        return dy[line]
    if line==1 or line==2:
        return line
    else:
        dy[line]=DFS(line-1)+DFS(line-2)
        return dy[line]
def solution(line):
    answer=DFS(line)
    return answer

print(solution(7))
