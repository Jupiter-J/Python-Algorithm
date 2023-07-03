
"""
queue사용
popleft왼쪽 하나를 꺼냄
꺼낸것을 좌우 노드로 값을 구한뒤 부모노드에 저장
"""

# from collections import deque
# def BFS():
#     Q = deque()
#     Q.append(1) #루트노드 넣기
#     L=0 #레벨시작
#     while Q: #비어있으면 멈춤
#         n = len(Q)
#         print(L, end = " : ") # 0: 1
#         for i in range(n):
#             v = Q.popleft() #1 꺼냄
#             print(v, end = "=")
#             for nv in [v*2 , v*2+1]: #2,3
#                 if nv>7:
#                     continue
#                 Q.append(nv) #Q = 2,3
#             print()
#             L+=1 #레벨 증가
#     BFS()

# from collections import deque
# def BFS(home):
#     ch=[0]*1001 #중복제거
#     Q = deque()
#     Q.append(0) #루트노드 넣기
#     ch[0]=1 #0은 탐색함
#     L = 0 #레벨
#     while Q:
#         n = len(Q)
#         for i in range(n):
#             x = Q.popleft() #부모노드
#             if x == home:
#                 return L
#             for nx in [x-1, x+1, x+5]:
#                 if nx >=0 and nx<=10000 and ch[nx]==0: #중복제거
#                     Q.append(nx)
#                     ch[nx]=1 #Q에 넣은값 체크
#         L+=1
# def solution(home):
#     answer= BFS(home)
#     return answer

from collections import deque
def BFS(home):
    ch=[0]*10001
    Q=deque()
    Q.append(0)
    L=0
    while Q:
        n = len(Q)
        for i in range(n):
            x = Q.popleft()
            if x==home:
                return L
            for nx in [x-1, x+0, x+5]:
                if nx>=0 and nx<=10000 and ch[nx]==0:
                    ch[nx]=1
                    Q.append(nx)
        L+=1
def solution(home):
    answer=BFS(home)
    return answer



print(solution(10))
# print(solution(14))
# print(solution(25))
# print(solution(24))
# print(solution(345))

