"""
1. 중복문자는 전체 문자(s)길이의 반이 넘어가지 않는다
2. 전체를 탐색하여 문자갯수를 점차 늘려나가기~길이의 반까지

O(n^2)
"""

s = "aabbaccc"
answer = len(s)
for x in range(1, len(s) // 2 + 1):
    #쪼갠 문자열의 길이
    char_len = 0
    #압축 문자열
    char = ''
    #반복 횟수
    cnt = 1
    #반복된 문자열 찾기(접차 증가)
    for i in range(0, len(s) + 1, x):
        tmp = s[i:i + x]
        #중복문자 확인
        if char == tmp:
            cnt += 1
        elif char != tmp:
            char_len += len(tmp)
            if cnt > 1:
                char_len += len(str(cnt))
            cnt = 1
            comp = tmp
    #길이 비교 (최종적으로 줄인 문자열 / 원래 문자열의 길이중 비교 )
    answer = min(answer, char_len)
print(answer)
