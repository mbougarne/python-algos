def merge_sort(data: list):
    if not isinstance(data, list):
        print(f'The data {data} MUST be type of list')
    
    if len(data) == 0 or len(data) == 1:
        return
    
    mid = len(data) // 2
    left = data[:mid]
    right = data [mid:]

    merge_sort(left)
    merge_sort(right)

    l = 0
    r = 0
    k = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            data[k] = left[l]
            l = l + 1
        else:
            data[k] = right[r]
            r = r + 1
        k = k + 1
    
    while l < len(left):
        data[k] = left[l]
        l = l + 1
        k = k +1
    
    while r < len(right):
        data[k] = right[r]
        r = r + 1
        k = k + 1

data = [87, 41, 23, 53, 20, 56, 6, 19, 8, 41]
print(data)
print(merge_sort(data))
print(data)