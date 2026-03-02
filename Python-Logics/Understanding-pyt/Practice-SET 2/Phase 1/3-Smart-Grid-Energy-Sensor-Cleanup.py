data = [[22, None, 25], [None, None, 19], [20, 21, 22]]

# Method 1: Using List Comprehension (No variables needed for iteration)
result = [
    sum(list(filter(lambda x: x is not None, daily_readings))) / len(list(filter(lambda x: x is not None, daily_readings)))
    for daily_readings in data
]
print(result)