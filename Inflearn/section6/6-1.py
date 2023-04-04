
"""
## 재귀함수 DFS - 깊이우선 탐색
반복문의 효과
자기 자신을 계속 호출 한다
스택을 활용해서 사용된다

"""
# # 재귀함수를 사용할때는 if-else 사용
# def DFS (x):
#     if x==0: #탈출
#         return
#     else:
#         DFS(x//2) #몫으로 호출 - 스택에 계속 쌓인다
#         print(x % 2, end='')  # 나머지
#
# n = int(input())
# DFS(n)
#

def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')

n = int(input())
DFS(n)
