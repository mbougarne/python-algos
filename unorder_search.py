def unorder_search(item, items: list):
    if not isinstance(items, list):
        print(f'The items {items} MUST be of type list')
        return
    
    for i in range(0, len(items)):
        if item == items[i]:
            return i
    return None

data = [87, 47, 23, 53, 20, 56, 6, 19, 8, 41]
print(unorder_search(20, data))