import numpy as np
import scipy.linalg as linalg
import array_to_latex as a2l
import fractions
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

#  p2
# A_flat = np.array([7,6,4,0,3,3,7,3,1]).astype(float)
A_flat = np.array([7, 6, 1, 4, 5, 1, 7, 7, 7]).astype(float)
# A_flat = np.array([12,12,0,0,3,0,-2,0,0,1,-1,0,0,0,0,1,0,0,1,1]).astype(float)

# p3

n = np.sqrt(A_flat.shape[0]).astype(int)
A = A_flat.reshape((n, n))
# A = A_flat.reshape((5, 4))

# b = np.array([[2, 0, 11]]).T
# # print(x.shape, b.shape)
# xbar = np.linalg.pinv(A) @ b
# print(xbar)
# print(A @ xbar)

P, L, U = linalg.lu(A)

print("P", P)
print("L", L)
print("U", U)

totex = lambda A : a2l.to_ltx(A, frmt = '{:.2f}', arraytype = 'bmatrix', mathform=True)



# U, s, VT = linalg.svd(A)

# U_tex = totex(U)

# sigma = np.zeros(A.shape)
# for i, sig in enumerate(s):
#     sigma[i, i] = sig
# sigma_tex = totex(sigma)

# VT_tex = totex(VT)

# print("sigma", sigma)

# print("U", U)
# print("VT", VT)