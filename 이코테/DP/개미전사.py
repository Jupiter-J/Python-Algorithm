"""
4
1 3 1 5

7
1 3 1 5 8 2 9
"""
n = int(input())
food = list(map(int, input().split()))

d = [0]*100
d[0] = food[0]
d[1] = max(food[0], food[1]) #두번째 칸을 공격 or 두번째칸을 공격하지 x

for i in range(2,n):
    #현재위치에 더큰값을 저장 = (전값[-1], 전전값[-2]+현재[0]) 비교
    d[i] = max(d[i-1], d[i-2] + food[i])
print(d[n-1])