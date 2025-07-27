"""
Given a string of n words, help Alex to find out how many times his name appears in the string.

Constraint: 1 <= n <= 200

Sample input: Hi Alex WelcomeAlex Bye Alex.

Sample output: 3

Explanation: Alex name appears 3 times in the string. Hi Alex WelcomeAlex

Bye Alex.
"""
def count_alex_occurrences(text):
    return text.count("Alex")


input_string = input("Enter a string: ")


count = count_alex_occurrences(input_string)
print("Number of times 'Alex' appears:", count)
