import numpy as np

def singular(row):
    return (np.sum(row != 0) == 2)

def replacement(array,i,j,k):
    new_array = array.copy()
    new_array[:,j] = new_array[:,j] + new_array[:,i]
    new_array = np.delete(new_array, i, axis=1)
    new_array = np.delete(new_array,k,axis=0)
    return new_array

def get_sets(row):
    positive = np.where(row == 1)[0]
    negative = np.where(row == -1)[0]
    return [set(positive),set(negative)]

def singular_reduction(array):
    output = array
    for k in range(array.shape[0]):
        row = array[k,:]
        if singular(row):
            i,j = np.where(row !=0)[0]
            print(i,j,k)
            output = replacement(array,i,j,k)
    return output

def transitive_reduction(array):
    new_array = array.copy()
    for k in range(new_array.shape[0]):
        row = new_array[k,:]
        sets = get_sets(row)
        for j in range(new_array.shape[0]-k-1):
            second_row = new_array[k+j+1,:]
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
                            other_set.remove(e)
                            second_other_set.remove(e)
                            l = list(other_set)[0]
                            m = list(second_other_set)[0]
                            return replacement(new_array,l,m,k)
    return new_array

def transitive_relations(array):
    new_array = array.copy()
    relations_list = []
    for k in range(new_array.shape[0]):
        row = new_array[k,:]
        sets = get_sets(row)
        for j in range(new_array.shape[0]-k-1):
            second_row = new_array[k+j+1,:]
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
                            if (k,k+j+1) not in relations_list:
                                relations_list.append((k,k+j+1))
    return relations_list
    
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
    array = np.array([[-1 , 1 , 0 , 0 , 1 ,-1  ,0 , 0],
 [ 1 , 0 , 0 ,-1,  1 , 0 ,-1 , 0],
 [ 1, -1 , 0 , 0 , 0 , 1 , 0 ,-1],
 [ 0 , 0 ,-1 , 1, -1 , 1 , 0 , 0],
 [-1  ,1 , 0 , 0,  0 , 0 , 1 ,-1],
 [ 0 , 0 , 1 ,-1 ,-1 , 0,  1 , 0],
 [ 0 ,-1 , 1 , 0 , 0, -1 , 0 , 1],
 [ 0 , 0, -1 , 1,  0 , 0, -1 , 1]])
    print(array)
    print(transitive_relations(array))
    T = replacement(array,4,7,7)
    print(transitive_relations(T))
        