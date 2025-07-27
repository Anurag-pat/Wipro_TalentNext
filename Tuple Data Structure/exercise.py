"""1 Write a program to print the 4th element from first and 4th element from last in a tuple"""
my_tuple = (5, 10, 15, 20, 25, 30, 35, 40)

print("4th element from start:", my_tuple[3])
print("4th element from end:", my_tuple[-4])

"""2 Write a program to check whether an element exists in a tuple or not."""
my_tuple = (1, 3, 5, 7, 9)
element = 5

if element in my_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")

"""3 Write a program to convert a list into a tuple."""
my_list = [10, 20, 30, 40]
my_tuple = tuple(my_list)
print("Converted tuple:",my_tuple)

"""4 Write a program to find the index of an item in a tuple."""
my_tuple = (100, 200, 300, 400, 500)
index = my_tuple.index(300)
print("Index of 300 is:",index)

"""5 Write a program to replace last value of tuples in a list to 100.

Sample list: [(10 , 20, 40), (40, 50, 60), (70, 80, 90)]

Expected Output:

[(10, 20, 100), (40, 50, 100), (70, 80, 100)]"""
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

updated_list = [t[:-1] + (100,) for t in sample_list]
print("Updated list:", updated_list)