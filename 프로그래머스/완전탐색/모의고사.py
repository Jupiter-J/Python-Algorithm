
"""
모의고사
* 수포자를 어떻게 넣을 것인지
* 정답 갯수 cnt 필요
"""

# def solution(answer):
#     std1 = [1, 2, 3, 4, 5]
#     std2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#     result = []
#     cnt = [0, 0, 0]
#
#     for idx, x in enumerate(answer):
#         if x == std1[idx % len(std1)]:
#             cnt[0] += 1
#         if x == std2[idx % len(std2)]:
#             cnt[1] += 1
#         if x == std3[idx % len(std3)]:
#             cnt[2] += 1
#
#     for idx, x in enumerate(cnt):
#         if x == max(cnt):
#             result.append(idx + 1)
#
#     return result



answer = [1,2,3,4,5]
std1 = [1, 2, 3, 4, 5]
std2 = [2, 1, 2, 3, 2, 4, 2, 5]
std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
result = []
cnt = [0, 0, 0]

for idx, x in enumerate(answer):
    if x == std1[idx % len(std1)]:
        cnt[0] += 1
    if x == std2[idx % len(std2)]:
        cnt[1] += 1
    if x == std3[idx % len(std3)]:
        cnt[2] += 1

for idx, x in enumerate(cnt):
    if x == max(cnt):
        result.append(idx + 1)
print(result)


