import numpy.linalg as linalg
import numpy as np
from create_matrix import left_matrix,right_matrix
from reduce_obj import *

M = np.transpose(left_matrix(12))
N = np.transpose(right_matrix(12))

# print(M-N)

T = M-N
op = [[]]
m = [T]

def test(op,new_op):
    if len(op) != len(new_op):
        return True
    else:
        for k in range(len(op)):
            if op[k] != new_op[k]: 
                return True
    return False

def reduction(m,op):
    if np.any(T):
        new_m = []
        new_op = []
        for k in range(len(m)):
            M = m[k]
            singular_rows = singular_rows(M)
            if singular_rows:
                row = singular_rows[0]
                i,j = get_singular_row_tuple(row)
                new_array = reduce(M,i,j,row)
                new_op_seq = op[k] + [row]
                new_m.append(new_array)
                new_op.append(new_op_seq)
            if not singular_rows:
                transitive_tuples = transitive_tuples(M)
            for tuple in transitive_tuples:
                pass
    else:
        return T,op

# reductions = [[]]
# print(T)
# while np.any(T):
#     T = clean(T)
#     print("cleaned")
#     print(T)
#     if T.shape != singular_reduction(T).shape :
#         T = singular_reduction(T)
#         print("sing")
#     elif T.shape != transitive_reduction(T).shape: 
#         T = transitive_reduction(T)
#         print("trans")
#     else: 
#         break
    # print(T)