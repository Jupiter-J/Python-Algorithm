
"""
2
홍길동 95
이순신 77
"""

# n = int(input())
# arr = []
# for _ in range(n):
#     name ,score = map(str, input().split())
#     arr.append((name,int(score)))
#
# s = sorted(arr, key=lambda v: v[1]) #오름차순 정렬 // 내림차순 정렬: (arr, key=lambda v: -v[1])
# for x in s:
#     print(x[0], end=' ')

n = int(input())
array = []
for i in range(n):
    input_data = input().split()
    array.append(input_data[0], int(input_data[1]))

array = sorted(array, key=lambda student: student[1])
for student in array:
    print(student[0], end=' ')