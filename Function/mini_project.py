"""
Write a Python function that accepts a hyphen-separated sequence of colors as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically.

Constraint: All the colors will be completely in either lower case or upper case.

Sample input 1: green-red-yellow-black-white

Sample output 1: black-green-red-white-yellow

Sample input 2: PINK-BLUE-TAN-PURPLE

Sample output 2: BLUE-PINK-PURPLE-TAN
"""
def sort_colors(color_sequence):
    
    color_list = color_sequence.split('-')

    
    color_list.sort()

    
    sorted_sequence = '-'.join(color_list)

    return sorted_sequence


"""
Create a Python module with the following functions:

Function Name

Task

ispalindrome(name)

Given the user name as input, this function should tell us whether the name is a palindrome or not.

count_the_vowels(name)

Given the user name as input, this function should tell us how many vowels are present in it.

frequency_of_letters(name)

Given the user name as input, this function should tell us how many times each letter appears in the name.

Note: name will be completely in either lower case or upper case.

Import the module in another python script and test the functions by passing appropriate inputs.

Sample input 1: bob

Sample output 1:

Yes it is a palindrome.
No of vowels: 1

Frequency of letters: b-2, 0-1

Sample input 2: marcel bentok tanaka

Sample output 2:

No it is not a palindrome.

No of vowels: 7

Frequency of letters: m-1, a-4, r-1, c-1, e-2, 1-1, b-1, n-2,t-2,0-1,k-2
"""

def ispalindrome(name):
    
    cleaned = name.replace(" ", "")
    if cleaned == cleaned[::-1]:
        return "Yes it is a palindrome."
    else:
        return "No it is not a palindrome."

def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in name if char in vowels)
    return f"No of vowels: {count}"

def frequency_of_letters(name):
    freq = {}
    for char in name:
        if char != ' ':
            freq[char] = freq.get(char, 0) + 1
    freq_list = [f"{k}-{v}" for k, v in freq.items()]
    return "Frequency of letters: " + ", ".join(freq_list)

