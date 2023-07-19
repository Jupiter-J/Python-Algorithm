
"""
왕실의 나이트
"""

# def solution(night):
#     answer=0
#     alpha = ['0','a','b','c','d','e','f','g','h']
#     dx = [-2, -1, 1, 2, 2, 1, -1, -2]
#     dy = [-1, -2, -2, -1, 1, 2, 2, 1]
#
#     #체스판 만들기 (숫자행, 알파뱃열)
#     for i in range(1,9):
#         for j in alpha:
#             if night == j+str(i):
#                 x=i
#                 y=alpha.index(j)
#                 for k in range(8):
#                     nx = x+dx[k]
#                     ny = y+dy[k]
#                     if nx>=1 and nx<=8 and ny>=1 and ny<=8:
#                         answer+=1
#     return answer
# print(solution("c1"))


def solution(night):
    answer=0
    x = int(night[1])
    y = int(ord(night[0])) - int(ord('a'))+1
    map_list = [(-2,-1), (-2,1), (-1,+2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]
    for step in map_list:
        nx = x+step[0]
        ny = y+step[1]
        if nx>=1 and nx<=8 and ny>=1 and ny<=8:
            answer+=1

    return answer
print(solution("a1"))