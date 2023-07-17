"""
숫자 카드게임1
"""

# n ,m = map(int, input().split())
# answer=0
# for i in range(n):
#     data = list(map(int, input().split()))
#     num = min(data)
#     answer = max(answer, num)
# print(answer)

def solution(num):
    answer=-2147000000
    for i in num:
        min_num = min(i)
        answer = max(answer, min_num)
    return answer

print(solution([[7,3,1,8],[3,3,3,4]]))
