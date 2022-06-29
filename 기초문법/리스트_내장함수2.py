
#리스트 부분 출력
from cgi import print_arguments


a=[23,12,36,53,19]
print(a[:3])
print(a[1:4])

#리스트 길이 len
print(len(a))

#하나씩 값을 출력1.
for i in range(len(a)):
    print(a[i], end=' ')
print()

#하나씩 값을 출력2.
for x in a:
    print(x, end=' ')
print()

# 홀수만 출력
for x in a:
    if x%2==1:
        print(x, end=' ')
print()

#(인덱스 번호, 값)까지 출력하고 싶을때 enumerate
for x in enumerate(a):
    print(x) 

# 괄호없이 인덱스번호, 값 출력하고 싶을 때 enumerate
for x in enumerate(a):
    print(x[0], x[1])

# 잘사용하는 enumerate *****
for index, vlaue in enumerate(a):
    print(index, vlaue)
print()



b=(1,2,3,4,5)
print(b[0])
# b[0]=7  <- b=(1,2,3,4) 일때는 튜플이라 에러! b=[1,2,3,4] 리스트일때는 가능!

'''
리스트와 튜플의 차이
[] = 리스트 , () = 튜플
리스트는 값 변경이 가능하지만 튜플은 불가능하다  
'''

# 리스트를 순회하며 전부 참인지 거짓인지 판별 all
# x가 전체 값을 순회 앞의 조건 (60>X)를 판별 
if all(60>x for x in a): 
    print("yes") #all은 모두가 조건이 true일때 true 반환
else:
    print("No")


# any 한번이라도 참이 있으면 참
if any(15>x for x in a):
    print("yes")
else:
    print("No")