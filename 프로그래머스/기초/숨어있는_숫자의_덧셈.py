
def solution(my_string):
    answer = 0
    for x in my_string:
        if x.isalpha():
            my_string = my_string.replace(x,' ')
    for i in my_string.split():
        answer+=int(i)
    return answer
print(solution("aAb1B2cC34oOp"))