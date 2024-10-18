def split_list(lst):

    mid = (len(lst) + 1) // 2


    first_part = lst[:mid]
    second_part = lst[mid:]

    return [first_part, second_part]


# Тестування програми з використанням прикладів
print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
print(split_list([]))