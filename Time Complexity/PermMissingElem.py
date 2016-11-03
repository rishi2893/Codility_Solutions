def solution(A):
    l = len(A)
    expected_sum = (l+2)*(l+1)/2
    actual_sum = 0
    for val in A:
        actual_sum += val
        
    return expected_sum - actual_sum

# print solution([1,3,2])