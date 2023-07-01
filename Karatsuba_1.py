from math import ceil


def len_finder(num) -> int:
    """Given an integer number, returns the number of digits in it."""
    return len(str(num))


def karatsuba(num1, num2):
    if num1 < 10 and num2 < 10:
        return num1 * num2

    n = max(len_finder(num1), len_finder(num2))
    m = ceil(n / 2)

    # Splitting num1 into high and low parts
    num1_high = num1 // (10 ** m)
    num1_low = num1 % (10 ** m)

    # Splitting num2 into high and low parts
    num2_high = num2 // (10 ** m)
    num2_low = num2 % (10 ** m)

    high_sum = karatsuba(num1_high, num2_high)
    low_sum = karatsuba(num1_low, num2_low)
    mid_sum = karatsuba(num1_high + num1_low, num2_high + num2_low) - high_sum - low_sum

    result = (high_sum * (10 ** (m * 2))) + (mid_sum * (10 ** m)) + low_sum

    return result


x = 5678
y = 1234
print(karatsuba(x, y))
