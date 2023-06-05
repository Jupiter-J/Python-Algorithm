
"""
카펫
yellow = wh
brown = (w+2)(h+2)-wh
brown = 2x + 2y +4
"""
def solution(brown, yellow):
    s = brown * yellow
    w,h = 0,0
    answer = []
    for i in range(1 , s+1):
        #yellow 가로 높이를 구하기
        if yellow % i ==0:
            w = yellow//i
            h = i
            #각 가로 높이의 *2 +4가 brown조건과 같을때 정답
            if 2*w + 2*h +4 == brown:
                answer.append(w+2)
                answer.append(h+2)
                break
    return answer