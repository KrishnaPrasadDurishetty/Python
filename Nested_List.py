A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]
C = [] # To rapresent output
for i in range(len(A)):
    S = [] # To add rows to the matrix
    for j in range(len(A[0])):
        S.append(A[i][j] + B[i][j])
    C.append(S)
print(C)
