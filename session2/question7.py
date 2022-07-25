
# 배열을 0으로 초기화하여 idx를 소수라고 생각한다
# 소수는 1이 아님으로 for는 i= 2~n까지 돈다 
# cnt 소수를 카운트
# 나온 소수값은 배수를 체크해줌(약수는 1과 자기자신만 가능) => 1로 체크되면 소수가 아니다 즉 0이 소수
n = int(input())
ch = [0]*(n+1) 
cnt=0

for i in range(2, n+1):
    if ch[i]==0: #0으로 체크 되면(소수)
        cnt+=1 #cnt+=1증가
        for j in range(i, n+1, i): #(start, end, step-숫자의 간격*배수)
            ch[j]=1
print(cnt)
