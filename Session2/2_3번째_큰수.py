#set자료구조는 중복을 제거한다


#N장, K번째큰수를 입력받
n, k = map(int, input().split())
#n만큼 값들 입력받
len = list(map(int, input().split()))
#정렬 -> 중복일 경우 어떻게 해결할 것인가
res = set() # set은 같은 값을 넣어도 한번만 들어가진다 
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(len[i]+len[j]+len[m]) #set은 add사용
res = list(res) #set은 sort기능이 없다! 그래서 다시 리스트화로 만들기 
res.sort(reverse=True) #내림차순은 resverse=True 를 붙여야한다. 보통 falut가 default라서 오름차순이 되는것! 
print(res[k-1])


