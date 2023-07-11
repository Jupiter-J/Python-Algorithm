

"""
최대부분 증가수열
"""

def solution(element):
    answer=0
    element.insert(0,0) #[0,5,3,7,8,6,2,9,4]
    dy=[0]*len(element)
    dy[1]=1
    for i in range(2, len(element)): #2~8
        max=0
        for j in range(i-1, 0, -1):
            if element[j]<element[i] and dy[j]>max:
                max=dy[j]
        dy[i]=max+1
        if dy[i]>answer:
            answer=dy[i]
    return answer

print(solution([5,3,7,8,6,2,9,4]))