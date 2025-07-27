"""1 Write a program to remove a given item from the set."""
my_set = {10, 20, 30, 40, 50}
my_set.remove(30)  
print("Set after removing 30:",my_set)

"""2 Write a program to create an intersection of sets."""
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1 & set2  
print("Intersection:",intersection)

"""3 Write a program to create an union of sets."""
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2  
print("Union:",union)

"""4 Write a program to find the maximum and minimum value in a set."""
my_set = {10, 25, 5, 40, 15}
print("Maximum value:", max(my_set))
print("Minimum value:",min(my_set))