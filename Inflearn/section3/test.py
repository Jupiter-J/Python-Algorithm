

p = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt=0
for i in range(p):
    if b[i]==p[i] and -1:
        cnt+=1
        while p[i]==b[i]:
            cnt+=1
    else:
        cnt=0

print(cnt)