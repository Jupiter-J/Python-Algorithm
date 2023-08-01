
"""
3
1 3 5
5
2 3 6 7 9
"""

# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))
#
# answer = a+b
# print(' '.join(map(str, sorted(answer))))

"""
정답코드
"""
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1 =p2 = 0
answer = []


while p1<n and p2<m:  # 같지 않으면~ 식의 조건을 했었는데 크기비교로 사용하기
    if a[p1]>=b[p2]: # 값이 같을경우 복수로 넣어야 함으로 한쪽만 처리 (굳이 if3개를 만들 필요 없음)
        answer.append(b[p2])
        p2+=1
    elif a[p1]<b[p2]:
        answer.append(a[p1])
        p1+=1

# 예외처리 - append를 사용했다가 형식이 달라짐
if p1<n:
    answer=answer+a[p1:]
if p2<n:
    answer=answer+b[p2:]
print(' '.join(map(str,answer)))
