def solution(my_string):
    answer = ''
    vowel = ["a","e","i","o","u"]
    for x in my_string:
        if x not in vowel:
            answer+=x
    return answer