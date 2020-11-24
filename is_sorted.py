data1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
data2 = [19, 41, 49, 53, 6, 87, 20, 23, 56, 8]

def is_sorted_list(items: list):

    if not isinstance(items, list):
        print(f'The items {items} MUST be of type list')
        return
    
    for i in range(0, len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True

def is_sorted_list_with_all(items: list):

    if not isinstance(items, list):
        print(f'The items {items} MUST be of type list')
        return
    
    return all(items[i] <= items[i + 1] for i in range(0, len(items) - 1))


print(is_sorted_list(data1))
print(is_sorted_list(data2))
print(is_sorted_list_with_all(data1))
print(is_sorted_list_with_all(data2))