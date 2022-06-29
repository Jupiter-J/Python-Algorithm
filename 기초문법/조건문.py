

# 조건문 if (분기else, 중첩)
x= 7
if x == 7:
    print("Lucky")


# 중첩 조건문
y =4
if y >=10: #y가 10이상인지 판별 참이면 아래로
    if y%2==1: #10 이상이면서 홀수인지 판별 참이면 아래로
        print("10이상의 홀수")


# 논리 연산자 (교집합 and)
# 0보다 크면서 10보다 작은 자연수인지 판별
z = 7
if z>0:
    if z <10:
       print("10보다 작은 자연수1") 

if z>0 and z<10:
    print("10보다 작은 자연수2")

if 0<z<10: #파이썬의 특징
    print("10보다 작은 자연수3")




# 분기 조건문

x=10
if  x>0:
    print("양수")
else:
    print("음수")

y=93
if Y>=90:
    print("A")
elif y>=80:
    print("B")
elif y>=70:
    print("C")
elif y>=60:
    print("D")
else:
    print("F")