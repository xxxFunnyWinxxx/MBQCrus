import numpy as np

CZ = np.array([[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, -1]])
                
CZ_tens = CZ.reshape((2, 2, 2, 2))


X = np.array([[0, 1],
             [1, 0]])
             
Y = np.array([[0, -1j],
             [1j, 0]])
             
Z = np.array([[1, 0],
             [0, -1]])


Z_basis = np.array([[1, 0],[0, 1]])
X_basis = 0.5 ** (1/2) * np.array([[1, 1],[1, -1]])
Y_basis = 0.5 ** (1/2) * np.array([[1, 1j],[1, -1j]])
