"""
5
2 4 5 1 3
"""

n = int(input())
arr = list(map(int, input().split()))
str_res = ""
answer=[]

lt=0
rt=len(arr)-1
last = 0
answer = ""
tmp = []

while lt<=rt:
    if arr[lt]>last:
        tmp.append((arr[lt], 'L'))
    if arr[rt]>last:
        tmp.append((arr[rt], 'R'))
    # 비교할필요 없이 오름차순으로 크기 정렬
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        answer=answer+tmp[0][1] #가장 작은 인덱스의 value값 저장
        last=tmp[0][0] #가장 작은 인덱스의 key값 저장
        if tmp[0][1]=='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()

print(len(answer)) #문자열 크기가 정답 갯수
print(answer)