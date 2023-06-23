
# def solution(n):
#     answer = []
#     d = 2
#     while d<=n:
#         if n%d==0:
#             answer.append(d)
#             n=n//d
#         else:
#             d+=1
#     answer = set(answer)
#
#     return list(answer)

"""
테케오류 - 재도전
"""
def solution(n):
    answer = []
    d = 2
    while d<=n:
        if n%d==0:
            if d not in answer:
                answer.append(d)
            n=n//d
        else:
            d+=1

    return answer


print(solution(17))