
# 최솟값 구하기1
arr = [5,3,7,9,2,5,2,6]
arrMin = float('inf') #파이썬의 무한대값으로 넣어 초기값이 들어오도록 한다
for i in range(len(arr)):
    if arr[i]<arrMin:
        arrMin=arr[i]
print(arrMin)

# 최솟값 구하기2
arrMin2 = float('inf') 
for i in range(len(arr)):
    if arr[i]<= arrMin2: #만약 같다 <= 를 하게되면 같은 값이 올 경우 뒤의값이 선택된다 
        arrMin=arr[i]

# 최솟값 구하기3
arrMin3 = arr[0] #무한대가 아닌 idx0으로 초기화
for i in range(len(arr)):
    if arr[i]< arrMin3: 
        arrMin=arr[i]

# 최솟값 구하기4
arrMin4 = float('inf')
for x in arr: 
    if arr[i]< arrMin4: 
        arrMin=arr[i]