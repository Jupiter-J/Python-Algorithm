
# Python Alogorithm Study
### 🥑 인프런의 "파이썬 알고리즘 문제풀이" 강의를 공부합니다

<br>
<br>

## 시간 복잡도

---
파이썬 프로그램에서는 2,000만 번~1억 번의 연산을 1초의 수행 시간으로 예측 가능하다
- 최상의 경우 : 오메가 표기법 (Big-Ω Notation)
- 평균의 경우 : 세타 표기법 (Big-θ Notation)
- 최악의 경우 : 빅오 표기법 (Big-O Notation)

### 빅오 표기법(Big-O)
빅오 표기법은 불필요한 연산을 제거하여 알고리즘분석을 쉽게 할 목적으로 사용된다
- `O(1)` : 입력자료의 수에 관계없이 일정한 실행시간을 갖음
- `O(logn)` : 입력자료의 수에 따라 시간이 흐를수록 시간이 조금씩 증가
- `O(n)` : 입력 자료의 수에 따라 선형적인 실행 시간이 걸리는 경우 - 입력자료마다 일정 시간 할당
- `O(nlogn)` : 큰 문제를 일정 크기 갖는 문제로 쪼개고(logn+logn+ .. + logn) 다시 그것을 모으는 경우
- `O(n^2)` : 이중 루프내에서 입력 자료를 처리할 때
- `O(n^3)` : 삼중 루프 내에서 입력자료 처리할 때

  > ![image](https://user-images.githubusercontent.com/73453283/221763949-305fbbb1-f9ea-489c-8818-a2ab59a5c961.png)
### 시간 복잡도가 빠른 순
`O(1) > O(logn) > O(n) > O(nlogn) > O(n^2) > O(n^3) > O(2^n) > O(n!)`

  > ![image](https://user-images.githubusercontent.com/73453283/221763168-bf0b52b1-e3d3-4f65-b0d6-e604a7b85fce.png)

### 시간 측정
```python
import time
start_time = time.time()
end_time = time.time()
print("time: ", end_time - start_time)
```

<br>
<br>

# 알고리즘

---
### 큐 Queue
- 입력 된 데이터가 가장 먼저 출력되는 구조 
- FIFO(First In, First Out)
- deque: 양방향에서 데이터 추가/제거 할 수 있는 자료구조
  ```python
  from collections import deque
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  a.sort()
  a = deque(a)
  ```

### 스택 Stack
- 스택은 나중에 입력 된 데이터가 먼저 출력되는 구조 
- LIFO(Last In, First Out)
  - push() : 맨뒤에 집어넣음
  - pop() : 맨 앞부분 꺼내고 반환 (제거 후 반환)
  - size(): 큐의 길이 반환
  - empty(): 큐가 비어있는지 유무 반환
  - front(): 큐의 맨앞 부분 원소 반환
  - back(): 큐의 맨뒷부분 원소 반환 (제거하지 않고 반환함)

### 그리디 Greedy
* 현재 상황에서 지금 당장 좋은것만 고르는 방법
* 그리디 알고리즘 문제는 자주 정렬 알고리즘과 짝을 이뤄 출제된다 

### 해시 Hash
- 해시는 데이터를 다루는 기법 중의 하나로, 검색과 저장을 빠르게하는 자료구조이다
- 데이터를 저장할 때 Key-Value형태로 데이터가 존재하고, Key값이 배열의 인덱스로 저장되기 때문에 검색과 저장이 빠르게 일어나게 된다.
> 해시는 언제 사용하는게 좋을까?
> 1. 리스트를 사용할 수 없을 때
> 2. 빠르게 접근/ 탐색이 필요할 때
> 3. 집계가 필요할 때

> Dictionary vs List
> * Dictionary : key/value를 가진다. 항상 순서대로 처리되는 것을 보장하지 않음
> * List :  index로 각 요소가 저장되고 저장되는 순서를 보장함
> ![image](https://user-images.githubusercontent.com/73453283/224475812-c58a5ea2-ef97-49e0-8a57-643973071d15.png)


### 힙 Heap
- 일종의 트리로 수의 집합에서 가장 작은 수(키)나 가장 큰 수만을 자주 꺼내올때 유용한 자료구조
- A가 B의 부모노드이면 A의 키값과 B의 키값 사이에는 대소 관계가 성립한다
  - 최소 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙
  - 최대 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙
  > ![image](https://user-images.githubusercontent.com/73453283/224475252-8ca5c616-1b87-4f85-bb96-27876a8f5597.png)
- 파이썬 heapq 모듈은 heapq (priority queue) 알고리즘을 제공한
  - heapq.heappush(heap, item) : item을 heap에 추가
  - heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
  - heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
<br>

## 재귀함수 DFS


<br>

## Python 리스트 자료형 정리

---
> ![image](https://user-images.githubusercontent.com/73453283/224476134-d4422b0a-c189-4823-96fe-bcb30029b9e2.png)


<br>
<br>

## Python 문법

---
- 정수를 문자로 바꿔 순환하기 
  ```python
  n = list(map(int, str(n)))
  ```
  - `str(n)` : 숫자를 문자열로 만들어줌
  - `map(int, str(n)`: 문자열로 되어있는 각 자릿수를 정수로 바꿈
  - `list`: list함수로 변환한다 

<br>

- 리스트 정수 초기화
  ```python
  dq= list(range(1,8))
  dq= [1,2,3,4,5,6,7]
  ```
- 리스트 표현식 - 튜플생성
  ```python
  people = [(pos , val) for pos, val in enumerate(list(map(int, input().split())))]
  # list(map(int, input().split())) = 입력받음  ex.[60,50,70]
  # pos=인덱스, val=값
  # 결과 ex.[(0,60),(1,50),(2,70)]
  
  print(people[0]) #(0,60)

  test=people[0] #튜플 특정값 출력
  print('인덱스:' ,test[0]) # 인덱스: 0
  print('값:' ,test[1])  #값: 60
  ```

<br>

- dictionary
  - 딕셔너리 타입은 immutable한 키(key)와 mutable한 값(value)으로 맵핑되어 있는 순서가 없는 집합이다.
  - 이 때, key 값은 절대로 변하지 않으며 value 값은 변경할 수 있다.
  - 튜플과 다르게 key-value 쌍 자체를 수정하거나 삭제할 수 있기 때문에 유용하게 사용가능
  ```python
  n = int(input())
  p = dict()
  for i in range(n):
      word=input()
      p[word]=1 #key:word , value:1로 담는다
  ```
  - `values()` : vlaue값으로 for문 반복
  - `itmes()` : key, value 한꺼번에 for문 반복
     ```python
    for key, val in p.items():
      if val==1:
          print(key)
          break
    ```   
  - `get()` : key로 vlaue 얻기 (입력받은 문자열의 알파벳을 카운트하기)
    ```python
    a = input()
    str1= dict()
    for x in a:
        str1[x]=str1.get(x, 0)+1
                    #x라는 key값이 없으면 0리턴, 있으면 value리턴
    print(str1)
    # input AbaAeCe
    # {'A': 2, 'b': 1, 'a': 1, 'e': 2, 'C': 1}
    ```
  - `keys()` : key 값들만 비교하기 
    ```python
    for i in a1.keys():
    if i in b2.keys():
        if a1[i]!=b2[i]:
            print("NO")
        break
    else:
        print("NO")
        break
    ```
- heapq (최소힙)
  - 기본적으로 최소힙을 사용한다 
  - 최대힙을 사용하고 싶을 경우 음수를 넣어서 변형하기 
    ```python
    import heapq as hq
    a=[]
    while True:
        n = int(input())
        if n==-1:
            break
        if n==0: #쵯솟값 출력
            if len(a)==0: #비어 있을경우 
                print(-1)
            else:
                print(hq.heappop(a)) #루트 노드값(최솟값 출력)
        else:
            hq.heappush(a, n) #a라는 리스트에 n값을 최소힙의 형태로 넣는다 
    ```

<br>

<br>

- 조건식
  - AND 조건 - A AND B : A와 B 둘다 참이어야 조건 성립
  - OR 조건 - A OR B : A와 B 둘중 하나라도 참이면 조건 성립
  - NOT 조건 - A NOT B : A와 B 둘다 아니어야 조건 성립
<br>
<br>

# 코테 면접

---
## 배열
같은 타입의 변수들로 이루어진 집합. 메모리의 연속공간에 값이 채워져있다
1. 장점
- 검색 성능이 좋다. 인덱스를 사용하여 원소에 바로 접근 할 수 있다
2. 단점
- 초기 사이즈만큼 메모리의 연속공간이 필요함으로 작은 공간은 버려질 수있어 메모리 활용에 비효율적이다
- 값의 삽입과 삭제에서 비효율적이다. 데이터 중간 지점에서 변동이 있을경우 모든 값을 이동시켜야함

## 연결리스트
값과 주소를 묶은 노드로 주소를 연결한 자료구조
1. 장점
- 주소로 연결되어있어 값을 삽입하거나 삭제하는 연산의 속도가 빠르다
- 선언할 때 크기를 별도로 지정하지 않는다. 
- 연속된 공간이 필요하지 않아 빈 공간을 활용할 수 있어 메모리 활용이 효율적이다
2. 단점
- 리스트 원소로 바로 접근이 불가능하다
- Head 주소로부터 순차 접근해야한다

## deque (덱) 자료구조
파이썬 라이브러리로 양쪽에서 값을 삭제 삽입이 가능하다
이중 연결 리스트로 양방향이다
