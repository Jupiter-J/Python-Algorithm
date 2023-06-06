
"""
join구문, lamda식 
"""


# def solution(numbers):
#     numbers= list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#
#     return str(int(''.join(numbers)))

# numbers = [6,10,2]
# numbers = list(map(str, numbers))
# numbers.sort(key=lambda x: x*3, reverse=True)
# print(str(int(''.join(numbers))))


def solution(numbers):
    #int list -> str list로 변환
    numbers= list(map(str, numbers))
    #내림차순 정렬/ 3, 30 우선순위를 바꾸기 위해 3자리 맞추기
    numbers.sort(key=lambda x: x*3, reverse=True)
    #반복되는 0제거를 위해 int형 변환
    return str(int(''.join(numbers)))