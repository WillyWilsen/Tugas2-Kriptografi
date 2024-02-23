from sympy import mod_inverse

# Read cipher from file
file_name = "cipher.txt"
with open(file_name, "r") as file:
  cipher = file.read()
cipher = cipher.replace("\n", "")

# Menggunakan fungsi invers_matrix dari Tugas 1 IF4020 Kriptografi

# Minor matrix
def minor_matrix(mat, i, j):
  return [row[:j] + row[j+1:] for row in (mat[:i] + mat[i+1:])]

# Determinant matrix
def determinant_matrix(mat):
  if len(mat) == 1:
    return mat[0][0]
  if len(mat) == 2:
    return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
  det = 0
  for i in range(len(mat)):
    det += ((-1) ** i) * mat[0][i] * determinant_matrix(minor_matrix(mat, 0, i))
  return det

# Cofactor matrix
def cofactor_matrix(matrix):
  size = len(matrix)
  cofactor_mat = [[0]*size for _ in range(size)]
  for i in range(size):
    for j in range(size):
      minor = minor_matrix(matrix, i, j)
      cofactor_mat[i][j] = ((-1) ** (i+j)) * determinant_matrix(minor)
  return cofactor_mat

# Adjoint matrix
def adjoint_matrix(matrix):
  cofactor_mat = cofactor_matrix(matrix)
  adjoint_mat = [[cofactor_mat[j][i] for j in range(len(cofactor_mat))] for i in range(len(cofactor_mat[0]))]
  return adjoint_mat

# Invers matrix
def invers_matrix(matrix):
  adjoint_mat = adjoint_matrix(matrix)
  adjoint_mat = [[adjoint_mat[i][j] % 26 for j in range(len(adjoint_mat))] for i in range(len(adjoint_mat[0]))]
  det = determinant_matrix(matrix) % 26
  invers_det = mod_inverse(det, 26)
  invers_mat = [[adjoint_mat[i][j] * invers_det % 26 for j in range(len(adjoint_mat))] for i in range(len(adjoint_mat[0]))]
  return invers_mat

# Mencari key dengan rumus K = C * P^(-1) mod 26
P = [[7, 11, 8], [4, 14, 7], [11, 0, 0]]
P_invers = invers_matrix(P)
C = [[14, 0, 22], [25, 20, 18], [6, 17, 2]]
K = [[0]*3 for _ in range(3)]
for i in range(3):
  for j in range(3):
    for k in range(3):
      K[i][j] += C[i][k] * P_invers[k][j]
    K[i][j] %= 26
print(K)
print(invers_matrix(K))