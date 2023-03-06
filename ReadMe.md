
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

 ![image](https://user-images.githubusercontent.com/73453283/221763949-305fbbb1-f9ea-489c-8818-a2ab59a5c961.png)
### 시간 복잡도가 빠른 순
`O(1) > O(logn) > O(n) > O(nlogn) > O(n^2) > O(n^3) > O(2^n) > O(n!)`

![image](https://user-images.githubusercontent.com/73453283/221763168-bf0b52b1-e3d3-4f65-b0d6-e604a7b85fce.png)

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
