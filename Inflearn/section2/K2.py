
# T = int(input())
#
# for t in range(T):
#     N,s,e,k= map(int, input().split())
#     a = list(map(int, input().split()))
#     a=a[s-1:e]
#     a.sort()
#     print("#%d %d" %(t+1, a[k-1]))

"""
2. k번째 수
입력 받기
- 한개로 입력 받기 : int(input())
- 한줄로 입력 받기 : map(int, input().split())
- 리스트로 입력 받기 : list(map(int, input().split()))
인덱스 추출
- print(a[1:5]) : 1,2,3,4번 인덱스 까지 추출
- print(a[s-1:e]) : 번째 수는 인덱스 보다 1크다. 그래서 -1씩 해줘야함
출력
- %f : 실수
- %d : 정수
- %s : 문자열
print("#(원하는 문자) %d(원하는 타입/변수1) %d(원하는 타입/변수2)" %(변수1, 변수2))
print("#%d %d" %(t+1, a[k-1]))
"""

T = int(input())
for t in range(T):
    N,s,e,k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1,a[k-1]))