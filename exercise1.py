def fine_largest(number):
    if not number:
        return None

    largest = number[0]

    for num in number:
        if num > largest:
            largest = num

    return largest        


print(fine_largest([3, 41, 56, 21, 76, 9]))
print(fine_largest([-10, -5, -2, -18]))