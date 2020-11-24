def quick_sort(data: list, first: int, last: int):

    if not isinstance(data, list):
        print(f'The data {data} MUST be of type list')
        return
    
    if not isinstance(first, int) or not isinstance(last, int):
        print(f'The args {first}, and {last} MUST be an index')
        return

    if first < last:
        # pi: Pivote Index
        pi = partitions(data, first, last)
        quick_sort(data, first, pi - 1)
        quick_sort(data, pi + 1, last)

def partitions(data: list, first: int, last: int):

    if not isinstance(data, list):
        print(f'The data {data} MUST be of type list')
        return
    
    if not isinstance(first, int) or not isinstance(last, int):
        print(f'The args {first}, and {last} MUST be an index')
        return

    #pv: Pivot Value
    pv = data[first]
    lower = first + 1
    upper = last
    done = False

    while not done:

        while lower <= upper and data[lower] <= pv:
            lower += 1
        
        while data[upper] >= pv and upper >= lower:
            upper -= 1
        
        if lower > upper:
            done = True
        else:
            data[lower], data[upper] = data[upper], data[lower]
    
    data[first], data[upper] = data[upper], data[first]

    return upper

data = [87, 47, 23, 53, 20, 56, 6, 19, 8, 41]
print(data)
print( quick_sort(data, 0, len(data) - 1) )
print(data)
