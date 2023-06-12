num_list = [1, 2, 3, 4, 5]

# answer = []
# odd, even=0,0
# for x in num_list:
#     if x%2==0:
#         even+=1
#     else:
#         odd+=1
# answer.append(even)
# answer.append(odd)
# print(answer)

"""
리펙토링
"""

answer = [0,0]
for n in num_list:
    answer[n%2]+=1
print(answer)
