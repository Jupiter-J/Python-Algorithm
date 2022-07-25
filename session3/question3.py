


a=list(range(21)) #0이 포함된 상태
for _ in range(10): #원래 i가 들어오는데 바로 돌리고싶때 _ 사용/ 10개구간씩 읽음
    s, e=map(int, input().split()) #입력된 값 만큼 구간을 구하고(e-s+1)//2  역순
    for i in range((e-s+1)//2):
        a[s+i], a[e-i]= a[e-i], a[s+i] #swap: a,b = b,a
#출력
a.pop(0) #0번인덱스 없애기
for x in a:
    print(x, end=' ')