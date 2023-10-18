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

print(A,"awdw", np.linalg.inv(A))