
"""
2. 숫자만 추출
.isdecimal() : 0~9로 이루어진 수인지 판별
# 숫자 뒤집기
    1. 일의 자리 구하기 : t=x%10
    2. 숫자 뒤집기 : res=res*10+t
    3. 다음 일의자리 구하기 : x=x//10
# 숫자 추출 후 자연수 만들기(첫 자리의 0은 무시된다)
    res=res*10+x
    문자형을 인트형으로 바꿀 경우 int(x)필요!
# 약수 판별
    범위는 1부터 시작
    (%) 나머지가 0일 경우 나누어 떨어지기 때문에 약수
    res%i
"""
# str = input()
# res=0
#
# for x in str:
#     if x.isdecimal():
#         res=res*10+int(x)
# cnt=0
# for i in range(1, res+1):
#     if res%i==0:
#         cnt+=1
# print(cnt)

str= input()
res=0

for x in str:
    if x.isdecimal():
        res=res*10+int(x)
print(res)
cnt=0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)

