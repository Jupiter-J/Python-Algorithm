
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


"""
# ## 2. 변수 입려과 연산자 ************************
"""
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

"""
# # 3. 조건문 ****************************
"""
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

"""
# # 4. 반복문 **********************************************
"""
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

"""
# # 5. 반복문을 이용한 문제풀이 ***************************************
"""
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

# # 3) N의 약수 출력하기 - end 줄바꿈 없이 옆으로 나열 출력
# k = int(input())
# for i in range(1, k+1):
#     if k%i==0:
#         print(i, end=' ')

"""
# # 6. 중첩 반복문 *********************************************
"""
# # 2중 for 문
# for i in range(5):
#     print('i:', i, sep='', end=' ')
#     for j in range(5):
#         print('j:', j, sep='',end=' ')
#     print()

# # 별찍기 - 정 사각형
# for i in range(5):
#     for j in range(5):
#         print("*", end=' ')
#     print() # 줄 바꿈
#
# # 별찍기 - 직각 삼각형
# for i in range(5):
#     for j in range(i+1):
#         print("*", end=' ')
#     print() # 줄 바꿈
#
# # 별찍기 - 역 삼각형
# for i in range(5):
#     for j in range(5-i):
#         print("*", end=' ')
#     print()

"""
# # 7. 문자열과 내장함수 **************************************************
"""
# # 문자열 대문자화 - upper()
# msg= "It is Time" #변수는 대문자화 되지 않고 그대로임
# print(msg.upper())
# # 문자열 소문자화 - lower()
# print(msg.lower())

# # 변수에 대문자화 하여 저장
# msg= "It is Time"
# tmp = msg.upper()
# print(tmp)
# # 특정 문자 찾기 - find() : 인덱스 번호 반환
# print(tmp.find('T'))
# # 특정 문자 찾아 횟수 - count() : 몇개인지 찾음 숫자 반환
# print(tmp.count('T'))
# # 범위 지정 - [:2] = 0-2까지 출력
# print(msg[:2])
# print(msg[3:5]) # [3:5] = 3-5까지 출력
#
# # 인덱스 길이 구하기 - 공백 포함
# print(len(msg))
# # 문자열 하나씩 출력 1
# for i in range(len(msg)):
#     print(msg[i], end=' ')
# # 문자열 하나씩 출력 2
# print()
# for x in msg:
#     print(x, end=' ')
#
# # 대소 문자 구별 - isupper(), islower()
# print()
# for x in msg:
#     if x.islower():
#         print(x, end=' ')
# # 알파벳 구별 - isalpha()
# print()
# for j in msg:
#     if j.isalpha():
#         print(j, end='')

# # 아스키 넘버 - ord() : 문자에 대한 아스키 번호 출력
# tmp='az'
# for x in tmp:
#     print(ord(x))
#
# # 숫자에 대응되는 문자 출력 - chr(숫자)
# tmp=65
# print(chr(tmp))

"""
# 8. 리스트와 내장함수(1) *******************************************************
"""
# # 리스트 , 배열 출력
# import random as r
# b=list()
# print(b)
#
# a=[1,2,3,4,5]
# print(a)
# # 인덱스 위치의 값을 출력
# print(a[0])
# # 리스트 초기화 list(range(범위))
# b=list(range(1,11))
# print(b)
# # 리스트 합치기
# c = a+b
# print(c)

# # 리스트 추가 - append(값)
# a=[1,2,3,4,5]
# b=list(range(1,11))
# c=a+b
# print(a)
# a.append(6)
# print(a)
#
# # 특정 위치에 리스트 추가 - insert(원하는 위치, 값)
# a.insert(3,7)
# print(a)
#
# # 리스트 꺼내기 - pop() 맨 뒤에서 꺼냄
# a.pop()
# print(a)
# a.pop(3) # pop(원하는 위치) 해당 위치에서 꺼냄
# print(a)
#
# # 특정 값을 지우기 - remove(지우고 싶은 값)
# a.remove(4)
# print(a)
# # 원하는 값의 인덱스 번호 찾기 - a.index(원하는 값)
# print(a.index(5))

# # 리스트의 값 모두 합치기 - sum()
# a=list(range(1,11))
# print(sum(a))
# # 리스트의 최대/최소 찾기 - max(), min()
# print(max(a), min(a))
# # 둘중에 최소값 찾는 법 - min(a ,b )
# print(min(7, 5 ,-3))
#
# # 리스트의 값 랜덤으로 섞기 - import random as , shuffle()
# import random as r
# r.shuffle(a)
# print(a)
#
# # 리스트 오름차순 정렬
# a.sort()
# print(a)
# # 리스트 내림차순 정렬
# a.sort(reverse=True)
# print(a)
# # 리스트 값 전부 삭제 - clear()
# a.clear()
# print(a)

"""
# # 9. 리스트와 내장함수(2) **********************************************
"""
# a=[23,12,36,53,19]
# print(a[:3]) # [:3] - 인덱스 0-2 출력
# print(a[1:4]) # [1:4] - 인덱스 1-3 출력
# # 리스트의 길이 구하기 - len()
# print(len(a))
#
# # 리스트 하나씩 출력1 - len(a), a[i]
# for i in range(len(a)):
#     print(a[i], end=' ')
# print()
# # 리스트 하나씩 출력2 - a, x
# for x in a:
#     print(x, end=' ')
#
# print()
#
# # 리스트 홀수 출력
# for x in a:
#     if x%2==1:
#         print(x, end=' ')
# print()
#
# # 리스트 인덱스 값도 같이 출력 - enumerate()
# for x in enumerate(a):
#     print(x)
# # ()없이 인덱스 값도 같이 출력
# for x in enumerate(a):
#     print(x[0], x[1])
# print()
#
# # ()없이 인덱스 값도 같이 출력 - 이 방법이 정석이다
# for index, value in enumerate(a):
#     print(index, value)
"""
리스트[]는 값을 변경 해도 괜찮다
튜플()일 경우 값 변경이 되지 않는다 
b=(1, 2, 3, 4, 5) - 소괄호()주의! 
print(b[0])
b[0]=7
"""

# a=[23,12,36,53,19]
#
# # all - 모든 조건이 true 일때 true 리턴
# if all( 60>x for x in a):
#     print("YES")
# else:
#     print("NO")
#
# # any - 한 번 이라도 true 일때 true 리턴 / 모두다 false 이면 false 리턴
# if any( 11>x for x in a):
#     print("YES")
# else:
#     print("NO")

"""
10. 2차원 리스트 생성과 접근
"""
# # 1차원 리스트 생성 : 0으로 초기화하여 크기 만큼 *3 넣기
# a=[0]*3
# print(a)

# # 2차원 리스트 생성 :1차원을 원하는 배열 수만큼 range() 넣기
# a=[[0]*3 for _ in range(3)]
# print(a)

# # 격자표 만들기
# a=[[0]*3 for _ in range(3)]
# print(a)
# a[0][1]=1
# print(a)
# a[1][1]=2
# print(a)
# # 격자표 확인
# for x in a:
#     print(x)
#
# # 격자표 출력
# for x in a: # x - 1차원 리스트 하나씩
#     for y in x: # y- 1차원 리스트 원소의 하나 하나 값
#         print(y, end=' ')
#     print()


"""
11. 함수 만들기 
함수는 항상 메인 스크립트 위에서 만들어 둘 것!!
def = 함수 정의
add = 함수 이름 
"""
# # def 함수 정의
# def add(a, b):
#     c=a+b
#     print(c)
# # 함수 실행
# add(3,2)
# add(5,7)

# # 함수로 여러개의 값 리턴 가능
# def add(a,b):
#     c=a+b
#     d=a-b
#     return c, d
# print(add(3,2))


# # 함수를 사용한 소수 출력
# def isPrime(x):
#     for i in range(2, x):
#         if x%i==0:
#             return False
#     return True
#
# a=[12,13,7,9,19]
# for y in a:
#     if isPrime(y):
#         print(y, end=' ')


"""
12. 람다 함수
변수에 할당을 꼭 해야한다 
내장 함수에 잘 사용된다 
"""
# # 일반 함수
# def plus_one(x):
#     return x+1
# print(plus_one(1))

# # 람다 함수 1.
# plus_two = lambda x: x+2
# print(plus_two(1))

# ## 람다 함수 2.
# def plus_one(x):
#     return x+1
# a=[1,2,3]
# print(list(map(plus_one, a)))

# # 람다 함수 3. - 잘 사용되는 방법 : 익명함수
# a=[1,2,3]
# print(list(map(lambda x: x+1, a)))
