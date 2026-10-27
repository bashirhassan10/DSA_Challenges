def fine_numbers(numbers, target):

    for i in range(len(numbers)):
        if number[i] == target:
            return i
    return -1 

print(fine_numbers([10, 25, 30, 45], 30))
print(fine_numbers([5, 8, 5, 9], 5))
print(fine_numbers([10, 20, 30], 99))    