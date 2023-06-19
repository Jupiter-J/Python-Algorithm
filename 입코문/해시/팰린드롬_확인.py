
"""
홀수인 빈도수가 2개이상이면 안된다
"""

from collections import defaultdict,Counter
def solution(s):
    cnt = 0
    dF = Counter(s)
    for key in dF:
        if dF[key] %2 ==1:
            cnt +=1
    return cnt <=1

print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))