
"""
계단오르기
"""
# def solution(step):
#     st=[0]*(step+1)
#     st[1]=1
#     st[2]=2
#     for i in range (3, step+1):
#         st[i]=st[i-1]+st[i-2]
#     return st[step]



# def DFS(step):
#     st=[0]*(step+1)
#     if step==1 or step==2:
#         return step
#     else:
#         st[step]= DFS(step-1)+DFS(step-2)
#     return st[step]
# def solution(step):
#     answer = DFS(step)
#     return answer
# print(solution(7))

"""
돌다리 건너기
"""

def solution(jump):
    dx=[0]*(jump+2)
    dx[1]=1
    dx[2]=2

    for i in range(3, jump+2):
        dx[i]=dx[i-1]+dx[i-2]
    return dx[jump+1]

print(solution(7))