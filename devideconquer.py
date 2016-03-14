import copy


def binary_search(source, wanted):
    """
    Fuction Description:
        This function search for a certain object in a acsending sequence using binary search.
    Parameter Type:
        source:
            A acsending sequence.
            Its elements can be compared using operator < <= == >= >.
        wanted:
            The object you want to search.
            With the same type as elements in source.
    """
    start = 0
    end = len(source)
    middle = (start + end) / 2    
    while end - start > 1:
        if source[middle] == wanted:
            index = middle
            while index >= 0 and source[index] == wanted:
                # this part find wanted element that first appears
                index = index - 1
            return index + 1
        elif source[middle] > wanted:
            end = middle
        else:
            start = middle
        middle = (start + end) / 2
    if source[middle] == wanted:
        return middle
    else:
        return -1


def naive_fibonacci(n):
    """
    Function Description:
        This function calculate the nth Fibonacci number, i.e. f(n)
        and return it.
        This function use the naive method to calculate.
    """
    if n < 0:
        print "wrong input!"
        return
    a = 1
    b = 1
    for i in range(2, n + 1, 1):
        # i starts from 2 to n
        c = a + b
        a = b
        b = c
    return c


def naive_matrix_multiple(a, b):
    """
    Function Description:
        This function calculate the product of matrix a and b
        and return the result.
        Use naive method with time complexity n^3
    """
    result = copy.deepcopy(a)
    n = len(a)
    for i in range(n):
        for j in range(n):
            result[i][j] = 0
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


def matrix_pow(matrix, n):
    """
    Function Description:
        This function calculate the nth power of matrix.
    Parameter Type:
        n: the power of the matrix
        matrix: given in the following form
        [
            [a11, a12, ..., a1n],
            [a21, a22, ..., a2n],
            ...
            [an1, an2, ..., ann]
        ]
    Return Type:
        Return the result of the power with the same format as
        matrix.
    """
    if n == 1:
        return matrix

    if n % 2 == 0:
        temp = matrix_pow(matrix, n / 2)
        return naive_matrix_multiple(temp, temp)
    else:
        temp = matrix_pow(matrix, n / 2)
        return naive_matrix_multiple(matrix, 
            naive_matrix_multiple(temp, temp))


def la_fibonacci(n):
    """
    Function Description:
        This function calculate the nth Fibonacci number, i.e. f(n)
        and return it.
        This function use linear algebra method, i.e.:

                                        n
        f(n + 1)    f(n)         1   1
                             =    
          f(n)    f(n - 1)       1   0

        To calculate the nth power of the 2*2 matrix, we apply
        devide and conquer method.

    """
    return matrix_pow([[1, 1], [1, 0]], n)[0][0]
