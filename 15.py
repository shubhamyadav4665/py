def matrix_input(rows, cols):
    matrix = []
    print("Enter the elements row-wise:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices should have the same dimensions for addition.")
        return None
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

def matrix_subtraction(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices should have the same dimensions for subtraction.")
        return None
    result = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Number of columns in the first matrix should be equal to the number of rows in the second matrix for multiplication.")
        return None
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    print("Matrix Operations Program")
    choice = input("Choose operation:\n1. Addition\n2. Subtraction\n3. Multiplication\nEnter choice (1/2/3): ")
    
    rows1 = int(input("Enter number of rows for matrix 1: "))
    cols1 = int(input("Enter number of columns for matrix 1: "))
    matrix1 = matrix_input(rows1, cols1)
    
    rows2 = int(input("Enter number of rows for matrix 2: "))
    cols2 = int(input("Enter number of columns for matrix 2: "))
    matrix2 = matrix_input(rows2, cols2)
    
    if choice == '1':
        result = matrix_addition(matrix1, matrix2)
    elif choice == '2':
        result = matrix_subtraction(matrix1, matrix2)
    elif choice == '3':
        result = matrix_multiplication(matrix1, matrix2)
    else:
        print("Invalid choice.")
        return
    
    if result:
        print("Resultant matrix:")
        print_matrix(result)

if __name__ == "__main__":
    main()
    