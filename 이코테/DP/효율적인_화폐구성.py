

"""
2 15
2
3
"""

n, m = map(int, input().split())  # 2, 5
coin = [] #   [2,3]
for i in range(n):
    a= int(input())
    coin.append(a)

d=[10001]*(m+1)
d[0]=0 # 아무것도 사용 안할경우 = 0

for i in range(n): #i: 화폐단위 0-2
    for j in range(coin[i], m+1) :  #j: 각각의금액 2-5
        if d[j-coin[i]]!= 10001: #INF가 아니면 만들 수 있는 값이다
            """
            i = 0~2 => i=0, coin[0]=2
            j = 2~7 => 금액구하기
            d[2-coin[0]] = 0 -> INF가 아님으로 만들 수 있다.
            d[2] = min(d[2], d[2-2]+1)
                   최솟값(10001, 1)
            d=[0, 10001, "1", 10001] <=2는 1개로 만들어짐 
            """
            d[j] = min(d[j],d[j-coin[i]]+1)

if d[m]== 10001:
    print(-1)
else:
    print(d[m])
