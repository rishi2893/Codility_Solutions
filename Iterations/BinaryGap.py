def solution(N):
    binrep = []  # to store binary representation of the numebr N
    while N>0:
        binrep.append(N%2)
        N = N/2
    
    max = 0
    curr = 0
    flag = 0
    for val in binrep:
        if val == 1 and flag == 1:
            if curr > max:
                max = curr
            curr = 0
        elif val == 1:
            flag = 1
        elif val == 0 and flag == 1:
            curr = curr + 1
    
    return max
            
# uncomment below line to check the answer on your local box
# print solution(1041) 
        