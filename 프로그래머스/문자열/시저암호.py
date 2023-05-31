
"""
A~Z: 65 ~ 90
a~z: 97 ~ 122
"""


def solution(s, n):
    #1. 리스트 만들기
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        #알파벳 처음 위치(대소문자 판별)
        corr = ord('A') if s[i].isupper() else ord('a')
        #문자를 숫자 변환 -> n을 더함 -> 다시 문자로 변환
        s[i] = chr((ord(s[i]) - corr + n) % 26 + corr)
    return ''.join(s)


def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i]== ' ':
            continue
        check = ord('A') if s[i].isupper() else ord('a')
        s[i]= chr((ord(s[i])- check +n) %26 +check)
    return ''.join(s)