
age = 23
def solution(age):
    answer = ''
    age_list = []

    # 알파벳 문자 배열 생성
    for i in range(97, 123):
        age_list.append(chr(i))
    # 문자열 자르기
    for x in str(age):
        answer += age_list[int(x)]
    return answer

"""
리펙토링
"""

def solution(age):
    # age = "2" "3"
    # i = 0, 1
    return ''.join([chr(int(i) + 97) for i in str(age)])