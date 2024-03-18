from create_matrix import * 

n = 30

M = np.transpose(left_matrix(n))
N = np.transpose(right_matrix(n))

vector_list = [[]]
for k in range(n):
    new_vector_list = []
    for vector in vector_list:
        new_vector_list.append(vector + [0])
        new_vector_list.append(vector+ [1])
    vector_list = new_vector_list

nullvectors = []
for vector in vector_list:
    result = np.dot(M-N,vector)
    if not np.any(result):
        nullvectors.append(vector)

for vector in nullvectors:
    print(vector)

# after_cleaning = []
# for vector in nullvectors:
#     new_vector = vector[1:-1]
#     if np.any(new_vector) and (np.any((1-np.array(new_vector))) or (n==6)):
#         if new_vector not in after_cleaning:
#             after_cleaning.append(new_vector)

# for vector in after_cleaning:
#     print([0] + vector + [0])

# vec = [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
# vec2 = [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0]
# vec3 = [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0]

# M = left_matrix(12)
# N = right_matrix(12)
# vec4 = [0,0,1,1,0,2,0,2,1,1,2,1]
# print(np.dot(M-N,np.array(vec4)))
# print(M-N)