

s=input()  #문자열은 그냥 받음
res=0
for x in s: #S를 X가 하나씩 접근 
    if x.isdecimal(): #알파벳이 아닌 숫자형태 
             #0을 무시하기 위해 X10   
        res= res*10 + int(x) #문자이기 때문에 숫자화시키기
print(res)
cnt=0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)