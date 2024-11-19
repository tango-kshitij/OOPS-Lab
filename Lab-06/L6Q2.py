def process_list(input_list):
    cubed_values = list(map(lambda x: x ** 3, input_list))
    return cubed_values

my_list = [1, 2, 3, 4, 5]
result = process_list(my_list)
print(result)
