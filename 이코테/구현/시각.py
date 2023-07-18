
"""
24시간 / 60분 / 60초
0~24
0~99
0~99
"""

def solution(n):
    answer=0
    for i in range(n+1):
        for m in range(60):
            for s in range(60):
                if '3' in str(i) + str(m) + str(s):
                    answer+=1
    return answer
print(solution(5))