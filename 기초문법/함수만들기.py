
# 함수를 만들때는 def 로 시작 
from tkinter import N
from turtle import rt


def add(a, b):
    c=a+b
    print(c)

add(3,2) # 함수 호출 !반드시 함수먼저 만들고 호출할것

def haha(a,b):
    c=a+b
    return c

print(haha(3,2)) # 함수에서 반환된 값을 바로 출력

#변수에 값을 대입하여 출력
x = haha(3,2)
print(x)

#여러개의 값을 리턴
def zara(a,b):
    c = a+b
    d = a-b
    return c ,d #튜플 자료구조로 리턴
print(zara(3,2))


# 소수만 출력하기
def isPrime(x):
    for i in range(2, x):
        if x%i==0: #1과 자기자신을 제외하는게 소수
            return False
    return True
n=[12,13,7,9,19]
for y in n:
    if isPrime(y):
        print(y, end= ' ')
