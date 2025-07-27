"""1.Write a program to count the number of upper and lower case letters in a String."""
text = "Hello World"
upper = 0
lower = 0

for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

"""2.Write a program that will check whether a given String is Palindrome or not."""
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not aPalindrome")

"""3.Given a string, return a new string made of n copies of the first 2 chars of the original str where n is the length of the string. The string length will be >=2.
If input is "Wipro" then output should be "WiWiwiwiwi"."""
text = "Wipro"
n = len(text)
result = text[:2] * n
print("Output:",result)

"""4 Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi"."""
text = "xHix"

if text.startswith('x'):
    text = text[1:]
if text.endswith('x'):
    text = text[:-1]

print("Output:", text)

"""5. Given a string and an integer n, return a string made of n repetitions of the last n characte the string. You may assume that n is between 0 and the length of the string inclusive. For exa if the inputs are "Wipro" and 3, then the output should be "propropro"."""
text = "Wipro"
n = 3
last_n_chars = text[-n:]
result = last_n_chars * n
print("Output:",result)