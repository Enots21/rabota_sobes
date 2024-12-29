def sum_of_digits(n: int) -> int:
    sum_digits = 0
    n_str = str(n)
    for i in range(len(n_str)):
        sum_digits += int(n_str[i])
    return sum_digits


print(sum_of_digits(167))
