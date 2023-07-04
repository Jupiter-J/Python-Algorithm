def solution(scoville, K):
    answer = 0
    while scoville[0]<K:
        scoville.sort()
        scovil = scoville[0] + (scoville[1] * 2)
        answer += 1
        new_box = scoville[2:]
        new_box.append(scovil)
        new_box.sort()
        scoville = new_box
    return answer


# import heapq
# def solution(scoville, K):
#     answer = 0
#     heapq.heapify(scoville) #기존의 리스트를 오름차순 heapQ로 변환
#     while scoville[0]<K:
#         new_s = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2) #list의 가장 작은 값을 return하며 삭제
#         heapq.heappush(scoville,new_s)  #list에 value를 삽입, 자동으로 정렬한다
#         answer += 1
#         if scoville[0]<K and len(scoville)==1:
#             return -1
#     return answer

print(solution([1, 2, 3, 9, 10, 12], 7))



