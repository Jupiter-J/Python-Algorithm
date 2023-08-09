"""
문자열 재정렬

K1KA5CB7
AJKDLSI412K4JSJ9D
"""

s = input()
answer=[]
num=0
for c in s:
    if c.isalpha():
        answer.append(c)
    else:
        num+=int(c)
answer.sort()

## 수정 - 예외처리
if num!=0:
    answer.append(str(answer))
print(''.join(answer))