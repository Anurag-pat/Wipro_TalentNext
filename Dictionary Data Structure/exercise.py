"""1 Write a program to add a key and value to a dictionary.
Sample Dictionary: {0: 10, 1: 20}

Expected Result (0: 10, 1: 20, 2: 30}"""
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print("Updated Dictionary:", my_dict)

"""2 Write a program to concatenate the following dictionaries to create a new one.

dic1={1:10, 2:20) dic2=(3:30, 4:40) dic3=(5:50,6:60)

Expected Result {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60)"""
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Method 1: Using update()
result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)

print("Concatenated Dictionary:", result)

"""3 Write a program to check if a given key already exists in a dictionary."""
my_dict = {1: 'a', 2: 'b', 3: 'c'}
key_to_check = 2

if key_to_check in my_dict:
    print(f"Key {key_to_check} exists.")
else:
    print(f"Key {key_to_check} does not exist.")

"""4 Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values."""
my_dict = {'a': 1, 'b': 2, 'c': 3}

print("Keys:")
for key in my_dict:
    print(key)

print("Values:")
for value in my_dict.values():
    print(value)

print("Keys and Values:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

"""5 Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys."""
square_dict = {}
for i in range(1, 16):
    square_dict[i] = i * i

print("Dictionary of squares:", square_dict)

"""6 Write a program to sum all the values in a dictionary, considering the values will be of int type."""
my_dict = {'a': 10, 'b': 20, 'c': 30}
total = sum(my_dict.values())
print("Sum of values:", total)