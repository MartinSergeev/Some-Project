def count_words(arr):
    return {key: arr.count(key) for key in arr}


def unique_words_count(arr):
    return len(count_words(arr))


def unigue2(arr):
    return len(set(arr))


def dedup(items):
    found = set()
    result = []

    for item in items:
        if item not in found:
            result.append(item)
            found.add(item)

    return result


def nan_expand(times):
    result = ""
    if times == 0:
        return ""
    while times > 1:
        result += "Not a "
        times -= 1
    result += "Not a Nan"
    return result
"to write new solve of problem nan_expand"


def iterations_of_nan_expand(expanded):
    count = expanded.count("Not a ")
    if expanded == "":
        return 0
    if (len(expanded) - 3) % len("Not a ") != 0:
        return False
    return count


def divisors(n):
    return [x for x in range(1, n + 1) if n % x == 0]


def sum_of_divisors(n):
    return sum(divisors(n))


def is_prime(n):
    return n + 1 == sum_of_divisors(n)


def prime_factorization(n):
    div = divisors(n)
    prime_div = [number for number in div if is_prime(number)]
    counts = []
    for numb in prime_div:
        count = 0
        while n != 1 and n % numb == 0:
            count += 1
            n /= numb
        counts.append(count)
    return [(div, cnt) for div, cnt in zip(prime_div, counts)]


def take_same(numbers):
    result = []
    cur = 0
    if not numbers:
        return []
    else:
        result.append(numbers[0])
        while cur < len(numbers) - 1 and numbers[cur] == numbers[cur + 1]:
            result.append(numbers[cur + 1])
            cur += 1
    return result


def group(numbers):
    result = []
    length = len(numbers)
    while length > 0:
        group = take_same(numbers)
        result.append(group)
        numbers = numbers[len(group):]
        length -= len(group)
    return result


def max_consecutive(items):
    return max([len(item) for item in group(items)])


def even(number):
    return number % 2


def group_by(func, seq):
    groups = {}
    for argument in seq:
        groups.setdefault(func(argument), []).append(argument)
    return groups


def prepare_meal(number):
    result = ""
    if number % 3 == 0:
        numSpam = max([n for n in range(1, number) if number % 3 ** n == 0])
        result += "spam " * numSpam
        if number % 5 == 0:
            result += "and eggs"
    elif number % 5 == 0:
        return "eggs"
    else:
        return "''"
    return result


def is_an_bn(word):
    symbol = 0
    while symbol < len(word) // 2:
        if not(word[symbol] == 'a' and word[symbol + len(word) // 2] == 'b'):
            return False
        symbol += 1
    return len(word) % 2 == 0


def transformation_card_number(number):
    strNumber = str(number)
    strNumber = strNumber[::-1]
    result = ""
    index = 0
    while index < len(strNumber):
        if index % 2 == 1:
            result += str(int(strNumber[index]) * 2)[::-1]
        else:
            result += strNumber[index]
        index += 1
    return result


def is_credit_card_valid(number):
    newNumber = transformation_card_number(number)
    sumDigits = sum(int(ch) for ch in newNumber)
    return sumDigits % 10 == 0


def goldbach(n):
    result = []
    for num in range(2, n // 2 + 1):
        if is_prime(num) and is_prime(n - num):
            result.append((num, n - num))
    return result


def sumRow_magic_square(matrix):
    sumRows = []
    for row in matrix:
        sumRows.append(sum(row))
    index = 0
    while index < len(sumRows) - 1:
        if sumRows[index] != sumRows[index + 1]:
            return 0
        index += 1
    return sumRows[0]


def transpose_matrix(m):
    lRow = len(m[0])
    return [[m[row][col] for row in range(0, lRow)] for col in range(0, lRow)]


def sum_diagonals_matrix(matrix):
    sumFD = 0
    sumBD = 0
    index = 0
    length = len(matrix[0])
    while index < length:
        sumFD += matrix[index][index]
        sumBD += matrix[length - index - 1][index]
        index += 1
    if sumFD == sumBD:
        return sumFD
    return 0


def magic_square(matrix):
    sum_row = sumRow_magic_square(matrix)
    sum_col = sumRow_magic_square(transpose_matrix(matrix))
    sum_diagonals = sum_diagonals_matrix(matrix)
    if sum_row == sum_col == sum_diagonals != 0:
        return True
    return False
