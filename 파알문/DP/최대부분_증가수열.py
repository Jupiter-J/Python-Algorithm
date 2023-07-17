

"""
최대부분 증가수열
"""

def solution(num):
    answer=set()
    for i in range(1, len(num)):
        x=max(num[i-1],num[i])
        if len(answer)==0:
            answer.add(num[i-1])
        elif answer[-1]< x:
            answer.add(max(num[i-1],num[i]))



    return answer

print(solution([5,3,7,8,6,2,9,4]))