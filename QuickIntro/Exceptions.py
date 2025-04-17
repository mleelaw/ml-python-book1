# TypeError
def add_numbers(a, b):
    try:
        result = a + b
        print(f"The result is: {result}")
    except TypeError as e:
        print(f"Please provide 2 integers as arguments when invoking this function")


add_numbers(5, "10")

# KeyError
my_dict = {"name": "Alice", "age": 30, "city": "New York"}


def get_value(dictionary, key):
    try:
        value = dictionary[key]
        print(f"The value for `{key}` is: {value}")
    except KeyError as e:
        print(f"Key Error: The key `{key}` does not excist in the dictionary")


get_value(my_dict, "name")
get_value(my_dict, "occupation")
