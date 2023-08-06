
"""
곱하기 혹은 더하기
02984
567
"""

# 처음에 0이면 무조건 합
# 도중에 0이면 앞부분은 합, 뒷부분은 곱
# 예시1 - 02984
# 예시2 - 002984
# 예시3 - 0020984

data = input()
result = int(data[0]) # 첫 번째값 무조건 넣기
for i in range(1, len(data)):
    num = int(data[i])

    # 현재값<=1 거나 합<=1이면 덧셈
    if num <= 1 or result <=1:
        result += num
    else:
        result *= num
print(result)


# s = input()
# snum = 0 #합
# for c in s:
#     if snum>0:
#         if int(c)==0:
#             snum+=int(c)
#         else:
#             snum*=int(c)
#     else:
#         snum+=int(c)
# print(snum)


