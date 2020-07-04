def main_menu():

    # this is the entry point of program through the main function
    # function that naviagate through the whole program

    user_choice = ""

    # dictionary acting as a switch case as to reduce numbers of if else statements
    menu_options = {0 : "exit()",
                    1 : "matrices_addition()",
                    2 : "matrix_multiplication()",
                    3 : "matrices_multiplication()",
                    4 : "matrix_transpose()",
                    5 : "print(matrix_determinant(matrix, matrix_rows, matrix_columns))",
                    6 : "print(matrix_inverse(matrix, matrix_rows, matrix_columns))"}

    # while loop to keep running program until user exits
    while user_choice != 0:

        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")

        user_choice = int(input("Your choice:"))
        
        if user_choice in (5, 6):
            matrix_info = second_matrix_init(True)
            matrix, matrix_rows, matrix_columns = matrix_info
            
        eval(menu_options[user_choice])

        print("")


def first_matrix_init():

    # function to initialize the first matrix

    first_matrix = []
    first_matrix_rows = 0
    first_matrix_columns = 0
    
    first_matrix_rows , first_matrix_columns = input("Enter size of first matrix:").split()
    first_matrix_rows = int(first_matrix_rows)
    first_matrix_columns = int(first_matrix_columns)
    
    print("Enter first matrix:")
    for rows in range(first_matrix_rows):
        temp_variable = input().split()
        for number in range(len(temp_variable)):
            if "." in temp_variable[number]:
                temp_variable[number] = float(temp_variable[number])
            elif "."  not in temp_variable[number]:
                temp_variable[number] = int(temp_variable[number])
        first_matrix.append(temp_variable)

    return (first_matrix, first_matrix_rows, first_matrix_columns)


def second_matrix_init(is_single_matrix):

    # function to initialize the first matrix
    # second matrix is used when operations are performed on single matrix only

    second_matrix = []
    second_matrix_rows = 0
    second_matrix_columns = 0

    # checks whether single matrix operation is being performed
    if is_single_matrix:
        second_matrix_rows , second_matrix_columns = input("Enter size of matrix:").split()
    else:
        second_matrix_rows , second_matrix_columns = input("Enter size of second matrix:").split()
    second_matrix_rows = int(second_matrix_rows)
    second_matrix_columns = int(second_matrix_columns)

    if user_choice in (2, 4, 5, 6):
        print("Enter matrix:")
    else:
        print("Enter second matrix:")

    for rows in range(second_matrix_rows):
        temp_variable = input().split()
        for number in range(len(temp_variable)):
            if "." in temp_variable[number]:
                temp_variable[number] = float(temp_variable[number])
            elif "."  not in temp_variable[number]:
                temp_variable[number] = int(temp_variable[number])
        second_matrix.append(temp_variable)

    return (second_matrix, second_matrix_rows, second_matrix_columns)


def matrices_addition():

    first_matrix_info = first_matrix_init()
    second_matrix_info = second_matrix_init(False)

    first_matrix, first_matrix_rows, first_matrix_columns = first_matrix_info
    second_matrix, second_matrix_rows, second_matrix_columns = second_matrix_info

    # checks if matrices addition possible
    if first_matrix_rows == second_matrix_rows and first_matrix_columns == second_matrix_columns:

        sum_matrix = []

        for rows in range(first_matrix_rows):
            sum_matrix.append([])
            for columns in range(first_matrix_columns):
                sum_matrix[rows].append(first_matrix[rows][columns] + second_matrix[rows][columns])

        print("The result is:")
        for rows in range(first_matrix_rows):
            for columns in range(first_matrix_columns):
                print(sum_matrix[rows][columns], end = " ")
            print("")
    else:
        print("The operation cannot be performed.")

    print("")


def matrix_multiplication():

    matrix_info = second_matrix_init(True)

    matrix, matrix_rows, matrix_columns = matrix_info

    constant = input("Enter constant:")
    if "." in constant:
        constant = float(constant)
        is_float = True
    elif "." not in constant:
        constant = int(constant)
        is_float = False

    for rows in range(matrix_rows):
        for columns in range(matrix_columns):
            if is_float is False:
                matrix[rows][columns] = int(matrix[rows][columns] * constant)
            else:
                matrix[rows][columns] *= constant

    print("The result is:")
    for rows in range(matrix_rows):
        for columns in range(matrix_columns):
            print(matrix[rows][columns], end = " ")
        print()

    print("")


def matrices_multiplication():

    first_matrix_info = first_matrix_init()
    second_matrix_info = second_matrix_init(False)

    first_matrix, first_matrix_rows, first_matrix_columns = first_matrix_info
    second_matrix, second_matrix_rows, second_matrix_columns = second_matrix_info

    # checks if matrices multiplication possible
    if first_matrix_columns == second_matrix_rows:
        product_matrix = []
        second_matrix = main_diagonal(second_matrix, second_matrix_rows, second_matrix_columns)

        for rows in range(first_matrix_rows):
            product_matrix.append([])
            for columns in range(second_matrix_columns):
                temp_unit = 0
                for row in range(len(first_matrix[rows])):
                    for column in range(len(second_matrix[columns])):
                        if row == column:
                            if "." not in str(first_matrix[rows][row]) or "." not in str(second_matrix[columns][column]):
                                temp_unit += int(first_matrix[rows][row] * second_matrix[columns][column])
                            else:
                                temp_unit += float(first_matrix[rows][row] * second_matrix[columns][column])
                product_matrix[rows].append(temp_unit)

        print("The result is:")
        for rows in range(first_matrix_rows):
            for columns in range(second_matrix_columns):
                print(product_matrix[rows][columns], end=" ")
            print()
    else:
        print("The operation cannot be performed.")

    print("")


def matrix_transpose():

    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")

    # dictionary acting as a switch case as to reduce numbers of if else statements
    transpose_type = {1 : "main_diagonal(second_matrix, second_matrix_rows, second_matrix_columns)",
                      2 : "side_diagonal(second_matrix, second_matrix_rows, second_matrix_columns)",
                      3 : "vertical_line(second_matrix, second_matrix_rows, second_matrix_columns)",
                      4 : "horizontal_line(second_matrix, second_matrix_rows, second_matrix_columns)"}

    type_number = int(input("Your choice:"))

    second_matrix_info = second_matrix_init(True)
    second_matrix, second_matrix_rows, second_matrix_columns = second_matrix_info

    second_matrix = eval(transpose_type[type_number])

    print("The result is:")
    for rows in range(second_matrix_rows):
        for columns in range(second_matrix_columns):
            print(second_matrix[rows][columns], end=" ")
        print("")


def main_diagonal(matrix, matrix_rows, matrix_columns):

    temp_matrix = []

    for columns in range(matrix_columns):
        temp_unit = []
        for rows in range(matrix_rows):
            temp_unit.append(matrix[rows][columns])
        temp_matrix.append(temp_unit)

    return temp_matrix


def side_diagonal(matrix, matrix_rows, matrix_columns):

    # sequence of algorithm of horiontal, main diagonal and again horizontal diagonal transpose
    # returns side diagonal transpose
    matrix = horizontal_line(matrix, matrix_rows, matrix_columns)
    matrix = main_diagonal(matrix, matrix_rows, matrix_columns)
    matrix = horizontal_line(matrix, matrix_rows, matrix_columns)

    return matrix


def vertical_line(matrix, matrix_rows, matrix_columns):

    temp_matrix = []

    for rows in matrix:
        temp_unit = rows[::-1]
        temp_matrix.append(temp_unit)

    return temp_matrix


def horizontal_line(matrix, matrix_rows, matrix_columns):

    temp_matrix = []

    counter = -1

    for _i in range(matrix_rows):
        temp_unit = matrix[counter]
        temp_matrix.append(temp_unit)
        counter -= 1

    return temp_matrix


def matrix_determinant(matrix, matrix_rows, matrix_columns):

    if matrix_rows == matrix_columns == 2:
        return ((matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]))

    is_triangle_matrix = check_if_triangle_matrix(matrix, matrix_rows, matrix_columns)

    if is_triangle_matrix is True:
        diagonal_element_product = 1
        for rows in range(matrix_rows):
            for columns in range(matrix_columns):
                if rows == columns:
                    diagonal_element_product *= matrix[rows][columns]
        return diagonal_element_product

    else:
        return laplace_expansion(matrix, matrix_rows, matrix_columns)


def check_if_triangle_matrix(matrix, matrix_rows, matrix_columns):

    upper_triangle_elements = []
    lower_triangle_elements = []
    diagonal_element_indexes = []
    for i in range(0, 111):
        diagonal_element_indexes.append([i, i])

    for rows in range(matrix_rows):
        for columns in range(matrix_columns):
            if rows != columns:
                if diagonal_element_indexes[rows] < [rows, columns]:
                    upper_triangle_elements.append(matrix[rows][columns])
                elif diagonal_element_indexes[rows] > [rows, columns]:
                    lower_triangle_elements.append(matrix[rows][columns])

    is_triangle_matrix = not(any(lower_triangle_elements)) or not(any(upper_triangle_elements))

    return is_triangle_matrix


def laplace_expansion(matrix, matrix_rows, matrix_columns):

    row = 0
    column = 0
    determinant = 0
    is_odd_turn = False

    while row < matrix_rows and column < matrix_columns:

        temp_matrix = []

        for rows in range(matrix_rows):
            temp_matrix.append([])
            for columns in range(matrix_columns):
                if row != rows and column != columns:
                    temp_matrix[rows].append(matrix[rows][columns])

        temp_matrix.remove([])
        temp_matrix_determinant = matrix_determinant(temp_matrix, len(temp_matrix), len(temp_matrix[0]))

        if is_odd_turn is False:
            posisitional_element = matrix[row][column]
        elif is_odd_turn is True:
            posisitional_element = -(matrix[row][column])
        is_odd_turn = not(is_odd_turn)

        determinant += (posisitional_element * temp_matrix_determinant)

        column += 1

    return determinant


def matrix_inverse(matrix, matrix_rows, matrix_columns):

    determinant = matrix_determinant(matrix, matrix_rows, matrix_columns)

    if determinant != 0:
        inverse = []
        adjacent_matrix = adjacent_of_matrix(matrix, matrix_rows, matrix_columns)

        for rows in range(matrix_rows):
            inverse.append([])
            for columns in range(matrix_columns):
                inverse[rows].append((1 / determinant) * adjacent_matrix[rows][columns])

        print("The result is:")
        for rows in range(matrix_rows):
            for columns in range(matrix_columns):
                print(inverse[rows][columns], end = " ")
            print("")
        print("")

    else:
        print("This matrix doesn't have an inverse.")
        print("")


def adjacent_of_matrix(matrix, matrix_rows, matrix_columns):

    adjacent_matrix = []
    row = 0
    column = 0
    while row < matrix_rows:

        column = 0
        adjacent_matrix.append([])

        while column < matrix_columns:

            temp_matrix = []

            for rows in range(matrix_rows):
                temp_matrix.append([])
                for columns in range(matrix_columns):
                    if row != rows and column != columns:
                        temp_matrix[rows].append(matrix[rows][columns])

            temp_matrix.remove([])

            if ((row + 1) + (column + 1)) % 2 == 0:
                temp_matrix_determinant = matrix_determinant(temp_matrix, len(temp_matrix), len(temp_matrix[0]))
            else:
                temp_matrix_determinant = -(matrix_determinant(temp_matrix, len(temp_matrix), len(temp_matrix[0])))

            adjacent_matrix[row].append(temp_matrix_determinant)

            column += 1

        row += 1
    
    return main_diagonal(adjacent_matrix, len(adjacent_matrix), len(adjacent_matrix[0]))

def main():
    main_menu()

if __name__ == "__main__":
    main()
