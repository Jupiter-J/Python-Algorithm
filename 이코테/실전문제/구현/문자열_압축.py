
"""

"""

def solution(s):
    answer = len(s)
    for x in range(1, len(s)//2+1):
        char_len = 0 #턴이 끝날때마다 초기화
        char = ''
        cnt = 1
        for i in range(0, len(s)+1, x):
            temp = s[i: i+x]
            if char == temp:   #앞뒤 같은 문자열일 경우 누적합
                cnt += 1
            elif char != temp: #앞뒤 다른 문자열일 경우 - 문자만 저장
                char_len += len(temp)
                if cnt > 1:    #누적된 값의 여부 확인 T: 누적한 중복문자열 길이만 더하기
                    char_len += len(str(cnt))
                cnt = 1        # F,나머지: 1로 초기화, 마지막 문자열 저장
                char = temp
        answer = min(answer, char_len) #턴이 끝나기전 이전턴과 길이비교
    return answer
print(solution("aabbaccc"))
print(solution("abcabcdede"))




# def solution(s):
#     answer = 0
#     cnt=1
#     word=''
#     #한자리씩은 완료함 -> 1~len(s)//2바퀴만큼 늘려서 확인해야함
#     j=1
#     ch = [0]*(len(s)//2)
#     while (j<=len(s)//2):
#         for i in range(1, len(s), j):
#             if s[i-1]==s[i]:
#                 cnt+=1
#             else:
#                 if cnt==1:
#                     word+=s[i]
#                 else:
#                     word+=str(cnt)+s[i-1]
#                     cnt=1
#         # ch[j] = len(word)
#         print(word)
#         j+=1
#
#     return answer
#
# print(solution("aabbaccc"))
# print(solution("abcabcdede"))
