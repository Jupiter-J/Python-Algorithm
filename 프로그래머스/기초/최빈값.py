

array = [1, 2, 3, 3, 3, 4]

result = [0]*len(array)

for x in array:
    if result[x]==0:
        result[x]+=1
    result[x]+=1
print(result.index(max(result)))



def solution(array):
    answer = 0
    result=[0]*(len(array)+1)
    for x in array:
        if result[x]==0:
            result[x]+=1
        result[x]+=1
    cnt=0
    for a in result:
        if a == max(result):
            cnt+=1
    if cnt>1:
        return-1
    return result.index(max(result))