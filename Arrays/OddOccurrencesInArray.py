def solution(A):
    """
    O(N) solution
    """
    result = 0
    for val in A:
        result = result ^ val # XOR property: a XOR a = 0, a XOR b XOR b = a XOR 0 = a
        
    return result


#def solution2(A):
#    """
#    O(NlogN) solution
#    """
#    A = sorted(A)  # Sorting takes O(NlogN) time
#    index = len(A) - 1
#    l = len(A)
#    i = 1
#    
#    while i < l:
#        if A[i] != A[i-1]:
#            index = i-1
#            break
#        i = i + 2
#    
#    return A[index]
#
#print solution([2,3,2,1,2,1,3])
#print solution2([2,3,2,1,2,1,3])
