def sum_of_array(arr):
    """Find sum of array"""
    return sum(arr)

def find_largest_element(arr):
    """Find largest element in array"""
    return max(arr)

def split_and_add_first_part(arr, k):
    """Split array and add first part to end"""
    if k > len(arr):
        return "k should be less than array length"
    
    first_part = arr[:k]
    second_part = arr[k:]
    return second_part + first_part

def add_matrices(matrix1, matrix2):
    """Add two matrices"""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have same dimensions"
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

if __name__ == "__main__":
    # Test array sum
    arr = [1, 2, 3, 4, 5]
    print("Array:", arr)
    print("Sum of array:", sum_of_array(arr))
    
    # Test largest element
    print("\nLargest element:", find_largest_element(arr))
    
    # Test split and add
    k = 2
    print(f"\nAfter splitting at {k} and adding first part to end:")
    print(split_and_add_first_part(arr, k))
    
    # Test matrix addition
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    print("\nMatrix 1:", matrix1)
    print("Matrix 2:", matrix2)
    print("Sum of matrices:", add_matrices(matrix1, matrix2)) 