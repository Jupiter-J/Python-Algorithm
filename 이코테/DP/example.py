
"""
top-down
"""
d = [0]*100

def pibo(x):
    print('f(' + str(x) + '),', end=' ')

    if x==1 or x ==2:
        return 1

    if d[x]!=0:
        return d[x]

    d[x]=pibo(x-1) + pibo(x-2)
    return d[x]

pibo(6)

"""
bottom-up
"""

d=[0]*100
d[1]=1
d[2]=1
n=99

for i in range(3 +n+1):
    d[i]=d[i-1] + d[i-2]
print(d[n])