def order_search(item, items: list):

    if not isinstance(items, list):
        print(f'The items {items} MUST be of type list')
        return

    items.sort()

    size = len(items) - 1
    lower = 0
    upper = size

    while lower <= upper:
        mid = (upper + lower) // 2

        if item == items[mid]:
            return mid
        
        if item > items[mid]:
            lower = mid + 1
        else:
            upper = mid - 1
    
    if lower > upper:
        return None


data = [87, 47, 23, 53, 20, 56, 6, 19, 8, 41]
print(order_search(53, data))