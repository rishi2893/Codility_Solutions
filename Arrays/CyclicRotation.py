def solution(A, k):
    """
    O(N) time complexity + O(1) space complexity
    k rotations of A[] = rotate whole array then rotate array A[1..k-1] then rotate array A[k...n]
    """
    n = len(A)  # length of array A
    if n == 0:
        return A
    k = k % n  # simplifying number of rotations
    
    i = 0
    while i < n/2:
        tmp = A[i]
        A[i] = A[n-i-1]
        A[n-i-1] = tmp
        i = i + 1
        
    i = 0
    while i < k/2:
        tmp = A[i]
        A[i] = A[k-i-1]
        A[k-i-1] = tmp
        i = i + 1
        
    i = k
    while i < (k+n)/2:
        tmp = A[i]
        A[i] = A[n+k-i-1]
        A[n+k-i-1] = tmp
        i = i + 1
    
    return A

#print solution([3,8,9,7,6], 8)