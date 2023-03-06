


"""
역수열

"""
import time
start_time = time.time()

n = int(input())
a = list(map(int, input().split())) # 역수열

seq=[0]*n
for i in range(n):
    for j in range(n):
        if a[i]==0 and seq[j]==0:
            seq[j]=i+1
            break
        elif seq[j]==0:
            a[i]-=1
for x in seq:
    print(x, end=' ')



end_time = time.time()
print("time: ", end_time - start_time)