def merge_and_sort_lists(list1, list2):
	final_list = list1 + list2
	final_list.sort()
	return final_list

def matrix_multiply(matrixA, matrixB):
    A, B = 0,1

    num_rows = [len(matrix) for matrix in [matrixA, matrixB]]
    if 0 in num_rows:
        return []

    num_cols = [len(matrix[0]) for matrix in [matrixA, matrixB]]
    if 0 in num_cols or num_cols[A] != num_rows[B]:
        return []

    result = [[]] * num_rows[A]
    for i in range(num_rows[A]):
        result[i] = [0] * num_cols[B]

    for row in range(num_rows[A]):
        for col in range(num_cols[B]):
            for i in range(num_cols[A]):
                result[row][col] += matrixA[row][i] * matrixB[i][col]

    return result
