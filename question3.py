
# n, k 입력받기 
# n개만큼 카드값 입력받기
# 3개를 뽑을 경우 + 중복 제거(set())

n, k = map(int, input().split())
a = list(map(int, input().split()))
res=set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i] + a[j] + a[m]) # 중복을 제거하면서 res =set() 자료구조에 저장
res=list(res) #set()은 sort()가 불가능하여 list로 벼경후 세우기
res.sort(reverse=True) #내림차순은 reverse
print(res[k-1])