import numpy as np

def extract_submatrix(matrix, rows_to_remove, cols_to_remove):
    submatrix = np.delete(matrix, rows_to_remove, axis=0)
    submatrix = np.delete(submatrix, cols_to_remove, axis=1)

    return submatrix