def solution(keyinput, board):
    x=y=0
    xarea = board[0]//2 #2
    yarea = board[1]//2
    for key in keyinput:
        # -2<=x<=2
        if x <=xarea and y<=yarea and x>=-xarea and y>=-xarea:
            if key =="up":
                y+=1
            elif key == "down":
                y-=1
            elif key == "left":
                x-=1
            elif key == "right":
                x+=1
        else:
             continue
    return [x,y]



print(solution(	["left", "left", "left", "right", "right", "right", "right"], [5, 5]))