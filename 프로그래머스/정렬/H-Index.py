

"""
다시풀기
"""
citations= [3, 0, 6, 1, 5]
answer = 0
# cnt=1
# citations.sort() #[0,1,3,5,6]
#
# for i in range(len(citations)): #0~4
#     for j in range(i+1, len(citations)):#1~4
#         if citations[j]-citations[i]>0:
#             cnt+=1 #기준값보다 인용횟수가 크면
#         if cnt==citations[i]:
#             print(citations[i])
#     cnt=1


citations.sort()
article_count = len(citations)

for i in range(article_count):
    if citations[i] >= article_count-i:
        print(article_count-i)

def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i]>= l-i:
            return l-i
    return 0

"""
enumerate
"""
def solution(citations):
    citations.sort()
    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            return len(citations)-idx
    return 0