from mat import *
import numpy as np

A = readm('A.csv')
b = readm('b.csv')

def solve(A, b):
    # YOUR CODE HERE
    A,b = np.array(A), np.array(b)
    n = len(A[0])
    x = np.array([0]*n)

    # 1.elimination
    for k in range(n-1): #pivot equation
        for j in range(k+1, n): #eleminate eq j
            lam = A[j][k]/A[k][k]
            # update A[j][k เป็นต้นไป]
            A[j,k:n] = A[j,k:n] - lam*A[k,k:n]
            # update b[j]
            b[j] = b[j] - lam*b[k] 

    # 2.back substitution
    for k in range(n-1, -1, -1):
        x[k] = (b[k] - np.dot(A[k,k+1:n], x[k+1:n]))/A[k,k]
    
    return x.flatten()

print( solve(A, b) )
