
# # 다중 변수 출력
# a, b, c = 3,2,5
# print(a,b,c)

# # 값 교환
# a, b = 10, 20
# print(a,b)
# a, b = b, a
# print(a,b)

# # 변수 타입
# a=12345
# print(a)
# print(type(a)) # 타입 출력

# # 출력방식
# print("number")
# a,b,c= 1,2,3
# print(a,b,c)
# # 문자 + 숫자 출력
# print("number", a,b,c)
# # 문자 띄어쓰기 주기 (sep = 각변수 사이를 ''에 맞게 실행하라)
# print(a,b,c, sep=', ')
# # 문자 줄바꿈
# print(a,b,c, sep='\n')
# # 문자 나란히 띄어쓰기 (end=' ')
# print(a, end=' ')
# print(b, end=' ')
# print(c)


# ## 2. 변수 입려과 연산자 ************************
# # 변수로 입력 받기 - input()
# a=input("숫자를 입력하세요: ")
# print(a)

# # 문자열 두개 입력 받기 - input().split()
# a, b = input("숫자를 입력하세요: ").split()
# print(a,b)

# # 두개의 값을 입력 받아 연산하기
# a,b = input("숫자를 입력하세요: ").split()
# print(a+b) # !문자열 두개로 붙음
# a=int(a) # 형변환 - int(a)
# b=int(b)
# print(a+b) # 형변환 후 연산을 해야 정수형으로 계산된다

# # 한번에 정수화 시키기 - map
# a,b = map(int, input("숫자로 입력하세요: ").split())
# print(a+b) # 덧셈 - 5+2
# print(a-b) # 뺄셈 - 5-2
# print(a*b) # 곱 - 5*2
# print(a/b) # 나누기 - 5/2 = 2.5
# print(a//b) # 몫 - 5//2 = 2
# print(a%b) # 나머지 - 5%2 = 1
# print(a**b) # 제곱 - 5x5 = 25

# # 실수 정수 사칙연산 - 실수 + 정수는 실수타입 (더 컨범위의 형으로 연산 결과가 나온다)
# a=4.3
# b=5
# c=a+b
# print(type(c))

# # 3. 조건문 ****************************
# # if 조건문
# x=7
# if x==7:
#     print("Lucky") # 4칸 들여쓰기
#     print("ㅎㅎ")

# # 중첩 if 문 1
# x=15
# if x>=10:
#     if x%2==1:
#         print("10이상의 홀수")

# # 중첩 if 문 2
# x=9
# if x>0:
#     if x<10:수
#         print("10보다 작은 자연수")

# # 중첩 if 문 합치기 - and
# x=7
# if x>0 and x<10:
#     print("10보다 작은 자연수")

# # 중첩 if 문 and 다른 버전
# x=7
# if 0<x<10:
#     print("10보다 작은 자연수")

# # if - else 문
# x=10
# if x>0:
#     print("양수")
# else:
#     print("음수")

# # if - else 문 - elif : 연속으로 조건일 때 - 하나만 참이면 바로 끝 : 우선순위 중요
# x=88
# if x>=90:
#     print('A')
# elif x>=80:
#     print('B')
# elif x>=70:
#     print("C")
# elif x>=60:
#     print("D")
# else:
#     print("F")

# # elif vs if - if의 경우 따로 따로 T,F를 나누기 때문에 여러번 결과값이 나옴
# x=88
# if x>=90:
#     print('A')
# if x>=80:
#     print('B')
# if x>=70:
#     print("C")

# # 4. 반복문 **********************************************
# # 범위값 출력하기 - range(a,b) a~b 사이의 값 출력
# a=range(10)
# print(list(a))

# # for 문
# for i in range(10): # i가 0,1,2,3,4,5-9까지 반복
#     print("hello", i)

# # for 문 감소로 - range(a, b, -1) a-b범위까지 -1만큼 감소 (음수는 모두 가능)
# for i in range(10, 0, -2):
#     print(i)

# # while 문 - 1-10 출력
# i=1
# while i<=10:
#     print(i)
#     i=i+1

# # while 문 감소 출력
# i=10
# while i>=1:
#     print(i)
#     i=i-1

# # break, continue
# # 무한반복
# i=1
# while True:
#     print(i)
#     i+=1

# # break - if문을 사용해서 break를 건다
# i=1
# while True:
#     print(i)
#     if i==10:
#         break
#     i+=1

# # continue - 홀 수 출력
# for i in range(1,11):
#     if i%2==0:
#         continue
#     print(i)

# # for - else 문 : for에서 break 당하면 else 넘김 / 정상 종료시 else 실행
# for i in range(1,11):
#     print(i)
#     if i==5:
#         break
# else:
#     print(11)

# # 5. 반복문을 이용한 문제풀이 ***************************************
# # 1) 1 부터 N까지 홀수 출력하기
# a = int(input())
# for i in range(1,a+1):
#     if i%2==1:
#         print(i)
#
# # 2) 1 부터 N까지의 합 구하기
# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print(sum)

# 3) N의 약수 출력하기 - end 줄바꿈 없이 옆으로 나열 출력
k = int(input())
for i in range(1, k+1):
    if k%i==0:
        print(i, end=' ')

