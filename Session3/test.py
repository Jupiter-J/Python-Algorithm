
#g0en2Ts8eSoft
#028
s=input() 
res=0
for x in s: #S를 X가 하나씩 접근 
    if x.isdecimal(): #알파벳이 아닌 숫자형태 
             #0을 무시하기 위해 X10   
        res= res*10 + int(x) #문자이기 때문에 숫자화시키기
print(res)

