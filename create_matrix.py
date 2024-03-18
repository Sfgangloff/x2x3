import numpy as np


def left_matrix(n):
    array = []
    for k in range(n//2):
        row = []
        for j in range(2*k):
            row.append(0)
        row.append(1)
        row.append(1)
        for j in range(n - 2*k-2):
            row.append(0)
        array.append(row)
    for k in range(n//3):
        row = []
        for j in range (3*k):
            row.append(0)
        row.append(1)
        row.append(1)
        row.append(1)
        for j in range(n - 3*k - 3):
            row.append(0)
        array.append(row)
    for k in range(n-n//2-n//3):
        row = []
        for j in range(n):
            row.append(0)
        array.append(row)
    return np.array(array)

def right_matrix(n):
    array = []
    for k in range(n//2):
        row = []
        for j in range(k):
            row.append(0)
        row.append(1)
        for j in range(n//2-k-1):
            row.append(0)
        for j in range(k):
            row.append(0)
        row.append(1)
        for j in range(n//2-k-1):
            row.append(0)
        array.append(row)
    for k in range(n//3):
        row = []
        for j in range(k):
            row.append(0)
        row.append(1)
        for j in range(n//3-k-1):
            row.append(0)
        for j in range(k):
            row.append(0)
        row.append(1)
        for j in range(n//3-k-1):
            row.append(0)
        for j in range(k):
            row.append(0)
        row.append(1)
        for j in range(n//3-k-1):
            row.append(0)
        array.append(row)
    for k in range(n-n//2-n//3):
        row = []
        for j in range(n):
            row.append(0)
        array.append(row)
    return np.array(array)

if __name__ == "__main__":
    print(np.transpose(right_matrix(6)))