
#반30명 수학점수를 어떻게 담을까 
#리스트: 일렬로 나열된 인덱스번호에 값을 저장 일일히 변수를 만들어 저장할 필요 없음

import random as r
b=list()
print(b)

a=[1,2,3,4,5]
print(a)
print(a[0]) #인덱스 출력

b=list(range(1,11)) #b라는 리스트에 1~11까지 초기화 range
print(b)

c=a+b #리스트끼리 합하면 합쳐진다
print(c)

#리스트에 인덱스 추가하기 append
print(a)
a.append(6)
print(a)

#특정 인덱스 지점에 값을 추가 insert
a.insert(3,7) #3번인덱스 위치에 7추가(나머지는 뒤로 밀려남)
print(a)

#인덱스 꺼내기pop()
a.pop()
print(a)
# 특정위치의 인덱스 값 꺼내기 pop(n)
a.pop(3)
print(a)

# 리스트에서 특정값 제거하기 remove
a.remove(4) #값이 없어지고 한칸씩 앞으로 이동
print(a)

#값이 인덱스의 어디에 있는지 확인하기 
print(a.index(5))
a=list(range(1,11)) #1~10까지 배열에 값 넣기
print(a)
print(sum(a)) #합출력 sum
print(max(a)) #가장 큰값을 찾아주는 함수 max
print(min(a)) #가장 작은값을 찾아주는 함수 min

#값 비교해서 최솟값 출력
print(min(7,5,15)) 

#값을 무작위로 섞기 shuffle
print(a)
r.shuffle(a)
print(a)

# 오름차순으로 정렬 sort()
a.sort()
print(a)

#내림차순 정렬 sort(reverse=True)
a.sort(reverse=True)
print(a)

#리스트에 있는값 모두 삭제
a.clear()
print(a)