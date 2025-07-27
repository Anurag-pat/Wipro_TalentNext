"""Project: 1
Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him.

He challenges you to find it out without seeing the content of the file. He has given hints to find it. Let's surprise him by breaking the challenge with our python code.

Hints to find the secret message:

1. The number of lines in the file tells you the meeting time.



Note: 1<= number of lines <= 24
If the number of lines is exceeding 12, you need to convert it to 12 hour

format. For example,

If the number of lines is 15, then the meeting time is 3 PM.

If the number of lines is 10, then the meeting time is 10 AM.

2. The word appearing for the maximum number of times tells you the meeting place.



Note: Meeting place will be a street name.

For example,

If the word Oxford appears for the maximum number of times, then meeting place is Oxford Street.

If the word Park appears for the maximum number of times, then meeting place is Park Street.


Sample output 1:

Meeting time: 9 AM

Meeting place: Park Street

Explanation: Number of lines is 9. The word park appears for the maximum of 15 times."""

def find_meeting_details(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    num_lines = len(lines)
    if num_lines <= 12:
        time = f"{num_lines} AM"
    else:
        time = f"{num_lines % 12 if num_lines % 12 != 0 else 12} PM"

    full_text = ""
    for line in lines:
        full_text += line.lower()

    
    punctuations = ['.', ',', '(', ')', '-', '"', ';', ':', '[', ']', '?', '!', "'", '“', '”']
    for p in punctuations:
        full_text = full_text.replace(p, '')

    words = full_text.split()
    
    
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    
    max_word = ""
    max_count = 0
    for word in word_count:
        if word_count[word] > max_count:
            max_count = word_count[word]
            max_word = word

    
    print(f"Meeting time: {time}")
    print(f"Meeting place: {max_word.capitalize()} Street")


find_meeting_details("sample1.txt")


