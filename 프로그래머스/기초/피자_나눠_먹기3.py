def solution(slice, n):
    if n%slice==0:
        return n//slice
    else:
        return n//slice+1



"""
리펙토링
"""
def solution(slice, n):
    d, m = divmod(n, slice)
    return d + int(m != 0)