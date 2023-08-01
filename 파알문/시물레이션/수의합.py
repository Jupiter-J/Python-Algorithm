"""
8 3
1 2 1 3 1 1 1 2
"""
n, m = map(int, input().split())
a = list(map(int, input().split()))

p1=0
p2=1
tot=a[0] #p1~p2전까지의 합
cnt=0
while True:
    if tot<m:
        if p2<n: #끝에 닿기 전까지 합하기
            tot+=a[p2]
            p2+=1
        else:
            break
    elif tot==m:
        cnt+=1 # 값 증가
        tot-=a[p1] #누적합 진행을 위해 처음값 빼기
        p1+=1 #한칸더 증가
    else:
        tot-=a[p1] #tot값이 크면 p1값 배기
print(cnt)


n, m = map(int, input().split())
a = list(map(int, input().split()))
p1=0
p2=1
answer=0
while p1<n:
    save = a[p1] + a[p2]
    if save<m:
        p2+=1
    elif save==m:
        answer+=1
        p1=p2
        p2+=1
        save=0
    else: #save>m:  저장값이 클경우에 누적합 처리를 제대로 못함
        p1=p2
        p2+=1
        save=a[p1]
print(answer)
