import numpy as np
# Parameter :
A=np.array([[4,-3,2],[6,2,5],[-1,-2,3]])
B=np.array([[3,4],[1,2],[5,6]])
U=np.array([[0],[2],[-4]])
V=np.array([[1],[3],[-3]])
# print(A+B)
# print(-2*A)
# print(B/3)
# print(V.T@B)
# print(np.linalg.solve(np.array([[2 , -1] ,[ -3 ,2]]),np. array ([1 ,0]) ))
M=np.diag([1,2,3])
print(M)


"""
vektoren
np.dot(v,w): skalarprodukt von v und w (v1*w1 + v2*w1...)
np.linalg.norm(v): länge des Vektors V
np.cross(v,w): kreuzprodukt von V und W

--------------

np.array[ [zeile 1], [zeile 2]... [zeile n]]

np.linalg.inv(Matrix): produziert die inverse einer Matrix
M=A.T: Matrix M = transposition von Matrix A
M = A@B: Matrix M = Matrix A _matrixprodukt_ Matrix B
np.zeros(n): n x n matrix mit nur nullen
np.eye(x,y): x spalten y zeilen mit nur nullen außer diagonale, da nur einser
np.linalg.inv(A) inverse von Matrix A
np.diag([a,b,c...]): Matrix mit zahlen a b c ... auf der Diagonalen
np.trace(A): Summe der Spur (Summe der Zahlen auf der Matrix diagonalen)
np.linalg.det(A) determinante der Matrix A
"""