def power_of_2_recursive(n):
    if n == 0:
        return 1
    else:
        return 2 * power_of_2_recursive(n - 1)

def power_of_2_iterative(n):
    result = 1
    for _ in range(n):
        result *= 2
    return result

def power_of_2_bitwise(n):
    return 1 << n

def power_of_2_exponent(n):
    return 2 ** n
