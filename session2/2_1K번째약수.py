
# 1.두개의 값을 입력받는다
    # 숫자가 띄어쓰기일 경우는 map을 사용 + 분리는 split() + 문자열을 받았기 때문에 int화

n, k = map(int, input().split())
# 2. 약수를 구하는 것이기 때문에 전체를 돌려서 나눈다
    #인덱스는 항상 +1까지
cnt =0
for i in range(1, n+1):
    if n%i ==0:
        cnt +=1
    if cnt ==k:
        print(i)
        break
# 3. for문을 다 돌아도 찾지 못하면 멈추게 
else:
    print(-1)