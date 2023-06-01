
# def solution(s):
#     answer = len(s)
#     for x in range(1, len(s) // 2 + 1):
#         char_len = 0
#         char = ''
#         cnt = 1
#         for i in range(0, len(s) + 1, x):
#             temp = s[i: i +x]
#             if char == temp: cnt += 1
#             elif char != temp:
#                 char_len += len(temp)
#                 if cnt > 1: char_len += len(str(cnt))
#                 cnt = 1
#                 char = temp
#         answer = min(answer, char_len)
#     return answer

s=110
print(bin(s))