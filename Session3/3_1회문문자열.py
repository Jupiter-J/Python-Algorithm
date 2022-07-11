
#대소문자 구별

n = int(input())
for i in range(n):
    s=input() #문자열 입력받기
    s=s.upper() #문자열 대문자화
    size = len(s) #문자열의 길이
    for j in range(size//2): 
        if s[j] != s[-1-j]: #0~1까지 돌기때문
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))