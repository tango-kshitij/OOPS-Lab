def cube_elements(*args):
    cubed_values = map(lambda x: x ** 3, args)
    return list(cubed_values)

result = cube_elements(1, 2, 3, 4, 5)
print(result)
