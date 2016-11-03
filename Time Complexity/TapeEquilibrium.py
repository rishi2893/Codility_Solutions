def solution(A):
    l = len(A)
    prefix_sum = [0]*l
    prefix_sum[0] = A[0]
    i = 1
    while i < l:
        prefix_sum[i] = prefix_sum[i-1] + A[i]
        i = i + 1
    
    least = abs(prefix_sum[0] - (prefix_sum[l-1] - prefix_sum[0]))
    
    i = 1
    while i < l-1:
        curr = abs(prefix_sum[i] - (prefix_sum[l-1] - prefix_sum[i]))
        if curr < least:
            least = curr
        i = i + 1
        
    return least

#print solution([3,1,2,4,3])
            
        