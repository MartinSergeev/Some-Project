def divisors(n):
    return [x for x in range(1, n + 1) if n % x == 0]


def sum_of_divisors(n):
    return sum(divisors(n))


def is_prime(n):
    return n + 1 == sum_of_divisors(n)


def prime_number_of_divisors(n):
    return is_prime(len(divisors(n)))


def contains_digit(number, digit):
    return bool([digit for ch in str(number) if digit == int(ch)])


def contains_digits(number, digits):
    return bool([digit for digit in digits if contains_digit(number, digit)])


def is_number_balanced(n):
    st = str(n)
    if len(st) % 2 == 0:
        sum1 = sum([int(ch) for ch in st[:len(st)//2]])
        sum2 = sum([int(ch) for ch in st[len(st)//2::]])
    else:
        sum1 = sum([int(ch) for ch in st[:len(st)//2]])
        sum2 = sum([int(ch) for ch in st[len(st)//2 + 1::]])
    return sum1 == sum2


def count_substrings(haystack, needle):
    return haystack.count(needle)


def zero_insert(n):
    result = ""
    nString = str(n)
    current = 0

    while current < len(nString) - 1:
        x = nString[current]
        y = nString[current + 1]
        result += nString[current]
        if x == y or (int(x) + int(y)) % 10 == 0:
            result += '0'
        current += 1

    result += y

    return int(result)


def sum_matrix(m):
    return sum(sum(row) for row in m)


def matrix_bombing_plan(m):
    result = {}
    indRow = 0
    for row in m:
        indCol = 0
        for cell in row:
            result[(indRow, indCol)] = 1
            indCol += 1
        indRow += 1
    return (result)

print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


"""
def matrix_bombing_plan(m):
    result = {}
    i = 0
    indRow = 0
    indCol = 0
    for row in m:
        while indCol < len(row):
            t = indRow, indCol
            print (t)
            result[t]
            print(result[t])
            indCol += 1
        indRow += 1
    return result

print(matrix_bombing_plan([[1,2,3],[4,5,6],[7,8,9]]))
"""
