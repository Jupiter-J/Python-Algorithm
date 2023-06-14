
rsp=0
def solution(rsp):
    answer = ''
    for x in rsp:
        if x =='2':
            answer+='0'
        elif x == '0':
            answer +='5'
        elif x == '5':
            answer +='2'
    return answer

"""
리펙토링
"""

def solution(rsp):
    compare = {'0':'5', '2':'0', '5':'2' }
    return ''.join(compare[i] for i in rsp)

print(solution(rsp))