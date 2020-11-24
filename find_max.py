data = [87, 41, 23, 53, 20, 154, 56, 6, 19, 8, 41]

def find_largest(items: list):

    if not isinstance(items, list):
        print(f'The items {items} MUST be of type list')
    
    if len(items) == 1:
        return items[0]
    
    op1 = items[0]
    op2 = find_largest(items[1:])

    return op1 if op1 > op2 else op2


print(find_largest(data))