def square_of_sum(number):
    total = 0
    for i in range(1, number + 1):
        total += i
    return total * total


def sum_of_squares(number):
    total = 0
    for i in range(1, number + 1):
        total += i * i
    return total


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)


# Example
print(square_of_sum(10))        # 3025
print(sum_of_squares(10))       # 385
print(difference_of_squares(10))# 2640