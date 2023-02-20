
"""
3. 카드 역배치
# swap 방법
    a, b=map(int, input().split())
    a, b=b ,a
# 배열 오름차 순 초기화
    a = list(range(21))
# 변수 없이 반복 하기
    for _ in range(10):
# 역순 배치 : 회전할 바퀴 수를 구함
    (e-s+1)//2
"""


# # 배열을 오름차 순으로 초기화 시키기
# a = list(range(21))
#
# # 변수 없이 반복 입력 받기
# for _ in range(10):
#     s, e = map(int, input().split())
#     for i in range((e-s+1)//2):
#         a[s+i], a[e-i]=a[e-i], a[s+i]
#
# # 출력
# a.pop(0)
# for x in a:
#     print(x, end=' ')


a = list(range(21))
for _ in range(a):
    s, e = map(int, input())
    for i in range((e-s+1)//2):
        a[s+i],a[e-i] = a[e-i],a[s+i]
a.pop(0)
for x in a:
    print(x, end=' ')
