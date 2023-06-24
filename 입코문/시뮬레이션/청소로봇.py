
# def solution(moves):
#     x=y=0
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     for ch in moves:
#         if ch == 'U':
#             x = x + dx[0]
#             y = y + dy[0]
#         elif ch == 'R':
#             x = x + dx[1]
#             y = y + dy[1]
#         elif ch == 'D':
#             x = x + dx[2]
#             y = y + dy[2]
#         else:
#             x = x + dx[3]
#             y = y + dy[3]
#     return [x,y]

"""
리펙토링
"""

# def solution(moves):
#     ch=['U','R','D','L']
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     x = y = 0
#     for c in moves:
#         for k in range(4):
#             if c == ch[k]:
#                 x=x+dx[k]
#                 y=y+dy[k]
#     return [x,y]

def solution(moves):
    x = y= 0
    ch = ['U','R','D','L']
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for k in moves:
        for d in range(4):
            if k == ch[d]:
                x=x+dx[d]
                y=y+dy[d]
    return [x,y]

print(solution('RRRDDDLU'))
# print(solution('DDDRRRDDLL'))
# print(solution('RRRRRRDDDDDDUULLL'))
# print(solution('RRRRDDDRRDDLLUU'))
