
# 문자열을 읽어서 앞으로 뒤로 같는지 확인
n = int(input())
for i in range (n):
    s=input() #문자열 하나 들어옴
    s=s.upper() #대문자화
    size = len(s) #비교를 해야하기 대문에 문자열 길이를 확인
    for j in range (size//2): #거꾸로 해도 같은지 확인하려면 반씩 나눠서 비교해야함
        if s[j]!=s[-1-j]: #idx가 뒤에서부터는 -1
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))
        



