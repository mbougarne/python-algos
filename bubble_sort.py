def bubble_sort(data: list):

    if len(data) == 0:
        print(f'Nothing to sort {data} is empty')
        return
    
    for i in range(len(data) - 1, 0, -1):

        for j in range(i):
            
            if data[j] > data[j + 1]:

                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def main():
    arr = [87, 41, 23, 53, 20, 56, 6, 19, 8, 41]
    sorted_array = bubble_sort(arr)
    print(sorted_array)

if __name__ == "__main__":
    main()