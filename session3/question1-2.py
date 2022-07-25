
# 문자열을 읽어서 앞으로 뒤로 같는지 확인
n = int(input())
for i in range (n):
    s=input() #문자열 하나 들어옴
    s=s.upper() #대문자화
    if s==s[::-1]: #reverse
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))

