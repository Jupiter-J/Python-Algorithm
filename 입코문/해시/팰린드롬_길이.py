
"""
홀수 갯수가 있을 때만 len(s)-cnt +1
"""
from collections import Counter
def solution(s):
    dF = Counter(s)
    cnt = 0
    for key in dF:
        if dF[key] %2 ==1:
            cnt+=1
    return len(s)-cnt +1 if cnt >0 else len(s)




print(solution("abacbaa"))
# print(solution("abaaceeffkckbaa"))
# print(solution("abcabbcc"))
# print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
# print(solution("aabcefagcefbcabbcc"))