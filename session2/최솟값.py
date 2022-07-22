

# 최솟값을 구할때 가장 작은 값을 두고 무조건 참이 되도록 해야함
# 그래야 최초의 값이 들어가고 뒤로 비교하면서 값을 구함 

arr= [5, 1, 3, 7, 9, 2 , 5, 2, 6]

#1. 최솟값을 지정하는 방법
arrMin=float('inf')
for i in range(len(arr)):
    if arr[i]<arrMin:
        arrMin=arr[i]
print('1 =' , arrMin)

#2. 배열의 첫째 값으로 지정하는 방법
arrMin = arr[0]
for i in range(1, len(arr)):
    if arr[i]<arrMin:
        arrMin=arr[i]
print("2 =" , arrMin)

#3. 축약
arrMin = arr[0]
for x in arr:
    if x<arrMin:
        arrMin=x
print("3 =" , arrMin)
