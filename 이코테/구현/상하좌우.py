
"""
5
R R R U D D
"""

"""
오류1
"""
# n = int(input())
# map_list = list(map(str, input().split()))
# x ,y = 1,1
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# for d in map_list:
#     if x>=1 and y>=1 and x<n and y<n:
#         if d=='U':
#             x = x + dx[0]
#             y = y + dy[0]
#         elif d=='R':
#             x = x + dx[1]
#             y = y + dy[1]
#         elif d=='D':
#             y = y + dy[3]
#             x = x + dx[3]
#         elif d=='L':
#             x = x + dx[4]
#             y = y + dy[4]
#     else:
#         continue #[0,4]로 막힘
#     print(x, y)

# n = int(input())
# map_list = list(map(str, input().split()))
# x ,y = 1,1
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# dir = ['U','R','D','L']
#
# for d in map_list:
#     for k in range(4):
#         if d == dir[k]:
#             nx = x+ dx[k]
#             ny = y+ dy[k]
#     if nx<1 or ny<1 or nx>=n or ny>=n:
#         continue
#     x = nx
#     y = ny
#     print(x, y)

"""
정답코드
"""

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
dir = ['U','R','D','L']
def solution(n, m):
    x,y=1,1

    for c in m:
        for k in range(4):
            if c==dir[k]:
                nx = x+dx[k]
                ny = y+dy[k]
        if nx<1 or ny<1 or nx>=n or ny>=n:
            continue
        x = nx
        y = ny
    return [nx, ny]

print(solution(5, "RRRUDD"))


