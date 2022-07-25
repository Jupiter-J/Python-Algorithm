

from unicodedata import decimal


s = input()
res=0
for x in s: #1. 숫자 추출 후 자릿수로 변환
    if x.isdecimal(): #0~9까지 숫자 판별
        res=res*10+int(x) #현재 문자열이기 때문에 int로 변환 => res*10+x 자릿수변환
print(res)
cnt=0
for i in range(1, res+1): #2. 변환된 숫자의 약수 구하기 (약수는 1부터!)
    if res%i==0:
        cnt+=1
print(cnt)
