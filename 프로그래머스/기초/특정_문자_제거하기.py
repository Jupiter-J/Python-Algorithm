my_string= "abcdef"
letter = "f"
def solution(my_string, letter):
    answer = ''
    for x in my_string:
        if x!= letter:
            answer+=x
    return answer

def solution(my_string, letter):
    return my_string.replace(letter, '')

