

"""
k번째 큰 수
중복제거 set, but 오름차순 불가
"""

# n, k = map(int, input().split())
# n_list = list(map(int, input().split()))
# res = set()
#
# # 전체 경우의 수를 구해야함
# for i in range(n):
#     for j in range(i+1, n):
#         for m in range(j+1, n):
#             res.add(n_list[i]+n_list[j]+n_list[m]) #중복 없이 리스트화 set
#
# res=list(res)
# res.sort(reverse=True) #내림차순
# print(res[k-1])


n , k = map(int, input().split())
a = list(map(int, input().split()))
answer = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            answer.add(a[i]+a[j]+a[m])

answer = list(answer)
answer.sort(reverse=True)
print(answer[k-1])