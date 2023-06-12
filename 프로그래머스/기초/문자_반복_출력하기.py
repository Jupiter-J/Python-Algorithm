

my_string="hello"
n=3

def solution(my_string, n):
    answer=""
    for x in my_string:
        answer+=x*n
    return answer

print(solution(my_string, n))

"""
리펙토링
"""
def solution(my_string, n):
    return ''.join(i*n for i in my_string)