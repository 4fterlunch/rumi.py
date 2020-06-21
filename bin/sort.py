def _merge_util(B, C, A):
    p = len(B)
    q = len(C)
    i = j = k = 0
    while i < p and j < q:
        if B[i] <= C[j]:
            A[k] = B[i]
            i = i + 1
        else:
            A[k] = C[j]
            j = j + 1
        k = k + 1
    if i == p:
        A[k: p + q] = C[j: q]
    else:
        A[k: p + q] = B[i: p]
    
def Merge_sort(A):
    if len(A) > 1:
        n = len(A)
        B = A[:n // 2]
        C = A[n // 2:]
        Merge_sort(B)
        Merge_sort(C)
        _merge_util(B, C, A)

