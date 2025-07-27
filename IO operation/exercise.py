"""1. Write a program to read the entire content from a txt file and display it to the user."""
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)



"""2.Write a program to read first n lines from a txt file. Get n as user input."""
n = int(input("Enter number of lines to read: "))
with open("sample.txt", "r") as file:
    for i in range(n):
        line = file.readline()
        if line == "":
            break  # End of file
        print(line, end="")

"""3. Write a program to accept input from user and append it to a txt file."""
data = input("Enter text to append to the file: ")
with open("sample.txt", "a") as file:
    file.write(data + "\n")
print("Data appended successfully.")


"""4. Write a program to read contents from a txt file line by line and store each line into a list."""
lines_list = []
with open("sample.txt", "r") as file:
    lines_list = file.readlines()

print("Lines as list:")
print([line.strip() for line in lines_list])



"""5.Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it."""
with open("sample.txt", "r") as file:
    words = file.read().split()
    longest_word = max(words, key=len)

print("Longest word:", longest_word)

"""6. Write a program to count the frequency of a user entered word in a txt file."""
word_to_search = input("Enter the word to count: ")
with open("sample.txt", "r") as file:
    content = file.read()
    words = content.split()
    count = words.count(word_to_search)

print(f"The word '{word_to_search}' appears {count} time(s).")