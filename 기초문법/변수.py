
# 변수입력과 연산자

a, b = map(int, input("숫자를 입력하세요: ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)  #나누기
print(a//b) # 몫
print(a%b) #나머지
print(a**b) #거듭제곱

# 형이 다른 값끼리 연산을 하면 더 큰 범위의 연산타입 형으로 바뀐다
c = 4.3
d = 5
e = c + d
print(e)