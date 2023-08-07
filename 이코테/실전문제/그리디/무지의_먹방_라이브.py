
# def solution(food_times, k):
#     answer = 0
#     while k> 0:
#         for i in range(len(food_times)):
#             if sum(food_times)==0:
#                 return -1
#             k -= 1
#             if k == 0:
#                 return food_times.index(1) #정확한 인덱스를 알아야함
#             if food_times[0]==0:
#                 food_times.pop(0)
#                 food_times.append(0)
#             food_times.append(food_times.pop(0) - 1)
#     return answer
# print(solution([3,1,2],5))


import heapq
def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        return -1

    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    sum_value = 0
    previous = 0

    length = len(food_times)
    #시간이 적게 걸리는 음식부터 확인
    while sum_value + ((q[0][0] - previous)* length) <=k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous)* length #이전의 먹었던 음식시간 차 * 남아있는 음식개수 곱
        length -= 1
        previous = now

    answer = sorted(q, key=lambda x: x[1])
    return answer[(k - sum_value)%length][1]

print(solution([3,1,2],5))