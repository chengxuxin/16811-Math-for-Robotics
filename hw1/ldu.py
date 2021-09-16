import numpy as np
import fractions
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})


def swaprow(A, i, j):
    temp = np.copy(A[j])
    A[j] = np.copy(A[i])
    A[i] = temp
    return A

def swapele(A, idx1, idx2):
    temp = A[idx2]
    A[idx2] = A[idx1]
    A[idx1] = temp
    return A

def ldu(A):
    #  only row interchanges
    n = A.shape[0]
    L = np.identity(n)
    P = np.identity(n)
    for i in range(n):
        if A[i][i] == 0: # swap row
            # print(A)
            col = A[i+1:, i]
            swap_row_idx = np.nonzero(col)[0][0]+i+1
            A = swaprow(A, i, swap_row_idx)
            P = swaprow(P, i, swap_row_idx)
            L = swaprow(L, i, swap_row_idx)
            L = swapele(L, (i, i), (i, swap_row_idx))
            L = swapele(L, (swap_row_idx, i), (swap_row_idx, swap_row_idx))
        for j in range(i+1, n):
            row = A[j]
            ratio = row[i] / A[i][i]
            A[j] = row - A[i] * ratio
            L[j, i] += ratio
    D = np.diag(np.diag(A))
    U = (A.T / np.diag(A)).T
    return P, L, D, U


# A_flat = np.array([1, -2, 1, 1, 2, 2, 2, 3, 4]).astype(float)
# A_flat = np.array([1, 1, 0, 1, 1, 2, 4, 2, 3]).astype(float)
A_flat = np.array([7, 6, 1, 4, 5, 1, 7, 7, 7]).astype(float)
# A_flat = np.array([7,6,4,0,3,3,7,3,1]).astype(float)
# A_flat = np.array([12,12,0,0,3,0,-2,0,0,1,-1,0,0,0,0,1,0,0,1,1]).astype(float)

n = np.sqrt(A_flat.shape[0]).astype(int)
A = A_flat.reshape((n, n))

P, L, D, U = ldu(A)

print("P", P)
print("L", L)
print("D", D)
print("U", U)
