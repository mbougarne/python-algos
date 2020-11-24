fruits = ["orange", "banana", "apple", "avocado", "kiwi", "apricot",
            "cherry", "grape", "coconut", "lemon", "mango", "peach",
            "pear", "strawberry", "pineapple", "apple", "orange", "pear",
            "grape", "banana"
        ]

filters = dict()

for key in fruits:
    filters[key] = 1

result = set(filters.keys())
print(result)