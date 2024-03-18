import numpy as np

def singular_rows(array):
    rows_list = []
    for k in range(array.shape[0]):
        row = array[k,:]
        if (np.sum(row != 0) == 2):
            rows_list.append(k)
    return rows_list

def get_singular_row_tuple(row):
    i = np.where(row == 1)[0]
    j = np.where(row == -1)[0]
    return i,j

def get_sets(row):
    positive = np.where(row == 1)[0]
    negative = np.where(row == -1)[0]
    return [set(positive),set(negative)]

def transitive_tuples(array):
    tuple_list = []
    for k in range(array.shape[0]):
        row = array[k,:]
        sets = get_sets(row)
        for j in range(array.shape[0]-k-1):
            second_row = array[k+j+1,:]
            second_sets = get_sets(second_row)
            for s in second_sets: 
                if s in sets: 
                    sets_copy = sets.copy()
                    sets_copy.remove(s)
                    second_sets.remove(s)
                    other_set = sets_copy[0]
                    second_other_set = second_sets[0]
                    for e in second_other_set:
                        if e in other_set:
                            second_other_set.remove(e)
                            other_set.remove(e) 
                            if (k,k+j+1) not in tuple_list:
                                tuple_list.append((k,k+j+1))
                            break
    return tuple_list

def reduce(array,i,j,k):
    new_array = array.copy()
    new_array[:,j] = new_array[:,j] + new_array[:,i]
    new_array = np.delete(new_array, i, axis=1)
    new_array = np.delete(new_array,k,axis=0)
    return new_array

def clean(array):
    new_array = array.copy()
    index_list = []
    for k in range(new_array.shape[0]):
        row = new_array[k,:]
        if not row.any():
            index_list.append(k)
    new_array = np.delete(new_array,index_list,axis=0)
    index_list = []
    for k in range(new_array.shape[1]):
        column = new_array[:,k]
        if not column.any():
            index_list.append(k)
    new_array = np.delete(new_array,index_list,axis=1)
    index_list = []
    for k in range(new_array.shape[0]):
        row = new_array[k,:]
        for j in range(new_array.shape[0]-k-1):
            other_row = new_array[k+j+1,:]
            if not (row - other_row).any() or not (row + other_row).any():
                index_list.append(k)
    index_list = list(set(index_list))
    new_array = np.delete(new_array,index_list,axis=0)
    return new_array


    

                            


if __name__ == "__main__":
    array = np.array([[1,-1,0,0,0],[0,1,-1,1,-1],[0,0,1,-1,0]])
    print(singular_rows(array))
    array = np.array([[-1 , 1 , 0 , 0 , 1 ,-1  ,0 , 0],
 [ 1 , 0 , 0 ,-1,  1 , 0 ,-1 , 0],
 [ 1, -1 , 0 , 0 , 0 , 1 , 0 ,-1],
 [ 0 , 0 ,-1 , 1, -1 , 1 , 0 , 0],
 [-1  ,1 , 0 , 0,  0 , 0 , 1 ,-1],
 [ 0 , 0 , 1 ,-1 ,-1 , 0,  1 , 0],
 [ 0 ,-1 , 1 , 0 , 0, -1 , 0 , 1],
 [ 0 , 0, -1 , 1,  0 , 0, -1 , 1]])
    print(array)
    print(transitive_tuples(array))
