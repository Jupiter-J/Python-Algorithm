
"""
1로 만들기
"""

# n = int(input())
# cnt=0
# while n>1:
#     if n%5==0:
#         cnt+=1
#         n=n//5
#     elif n%3==0:
#         cnt+=1
#         n=n//3
#     elif n%2==0:
#         cnt+=1
#         n=n//2
#     else:
#         cnt+=1
#         n-=1
# print(cnt)


# #DFS로...
# min_value = 2147000000
# def DFS(v, n):
#     global min_value
#     if n==1:
#         return
#     else:
#         if n%5==0:
#             DFS(v+1, n=n//5)
#         elif n%3==0:
#             DFS(v+1, n=n//3)
#         elif n%2==0:
#             DFS(v+1, n=n//2)
#         else:
#             DFS(v+1, n=n-1)
# def solution(n):
#     return DFS(0, n)
# print(solution(26))

"""
bottom-up
"""


def solution(n):
    answer=0
    d=[0]*30001 #저장장소
    for i in range(2, n+1): #2-6까지 범위
        #1을 뺄 경우 , +1 경우의수
        d[i]= d[i-1] +1

        """
        2,3,5로 나눠질때 min[저장된값, 현재값+(1경우의 수)] 비교
        a(i) = min(a(i-1), a(i/2), a(i/3), a(i/5))+1
        -1,/2,/3,/5 계산한 값중 가장 작은 값의 경우를 비교해 +1을 해준다 
        """
        if i%2 == 0:
            d[i]=min(d[i], d[i//2]+1)
        if i%3 == 0:
            d[i]=min(d[i], d[i//3]+1)
        if i%5 == 0:
            d[i]=min(d[i], d[i//5]+1)
    return d[n]

print(solution(6))