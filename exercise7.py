def reverse_list(items):
    reuslt = []

    for i in range(len(items) -1, -1, -1):
        reuslt.append(items[i])

    return reuslt

print(reverse_list([1, 2, 3, 4]))
print(reverse_list(["a", "b", "c"]))        