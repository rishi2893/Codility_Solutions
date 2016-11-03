def solution(X, Y, D):
    ans = (Y - X) / D
    rem = (Y - X) % D
    if rem == 0:
        return ans
    return ans + 1

#print solution(10,85,30)