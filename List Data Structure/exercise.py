"""
1 Write a program to create a list of 5 integers and display the list items. Access individual elements through index."""
my_list = [10, 20, 30, 40, 50]
print("List:", my_list)

print("First element:", my_list[0])
print("Third element:",my_list[2])

"""2 Write a program to append a new item to the end of the list."""
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print("List after append:",my_list)

"""3 Write a program to reverse the order of the items in the list."""
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print("Reversed list:",my_list)

"""4 Write a program to print the number of occurrences of a specified element in a list."""
my_list = [1, 2, 3, 2, 4, 2, 5]
count = my_list.count(2)
print("Number of occurrences of 2:",count)

"""5 Write a program to append the items of listi to list2 in the front."""
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list2 = list1 + list2
print("Combined list:",list2)

"""6 Write a program to insert a new item before the second element in an existing list."""
my_list = [10, 20, 30, 40]
my_list.insert(1, 15)  
print("List after insertion:",my_list)

"""7 Write a program to remove the item from a specified index in a list."""
my_list = [10, 20, 30, 40, 50]
index_to_remove = 2
my_list.pop(index_to_remove)
print("List after removing item at index 2:",my_list)

"""8 Write a program to remove the first occurrence of a specified element from a list."""
my_list = [10, 20, 30, 20, 40]
my_list.remove(20)  
print("List after removing first occurrence of 20:", my_list)