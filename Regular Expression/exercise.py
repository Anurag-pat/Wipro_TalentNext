import re
"Write a program to find check if a String has only octal digits. Give string ['789','123','004']"

strings = ['789', '123', '004']

def is_octal(s):
    return all(char in '01234567' for char in s)


for s in strings:
    if is_octal(s):
        print(f"'{s}' contains only octal digits.")
    else:
        print(f"'{s}' does NOT contain only octal digits.")


"Extract the user id, domain name and suffix from the following email addresses. emails = zuck@facebook.com sunder33@google.comjeff42@amazon.com"

import re

emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

pattern = r'([\w\d]+)@([\w\d]+)\.([a-z]+)'

matches = re.findall(pattern, emails)

for user_id, domain, suffix in matches:
    print(f"User ID: {user_id}, Domain: {domain}, Suffix: {suffix}")



"""3.Split the following irregular sentence into proper words

A, very M sentence very; irregular_sentence ## expected outout: A very very irregular sentence"""



sentence = """A, very M sentence very; irregular_sentence"""

cleaned = re.sub(r'[^\w\s]', ' ', sentence)   
cleaned = re.sub(r'_', ' ', cleaned)          
cleaned = re.sub(r'\s+', ' ', cleaned).strip()  

print(cleaned)



"""4.Clean up the following tweet so that it contains only the user's message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.

#tweet='''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej@px0d cc: @garybernhardt #rstats'''

##desired output 'Good advice What I would do differently if I was learning to code today'"""


tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej@px0d cc: @garybernhardt #rstats'''

tweet = re.sub(r'\bRT\b|\bcc\b', '', tweet)


tweet = re.sub(r'@\w+|#\w+|http\S+', '', tweet)


tweet = re.sub(r'[^\w\s]', '', tweet)


tweet = re.sub(r'\s+', ' ', tweet).strip()

print(tweet)


"""5.Extract all the text portions between the tags from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.html

Code to retrieve the HTML page is given below:

import requests

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html") r.text # html text is contained here
desired output['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph!', 'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']"""

import requests
from bs4 import BeautifulSoup

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
soup = BeautifulSoup(r.text, 'html.parser')

text_list = [tag.get_text() for tag in soup.find_all() if tag.get_text().strip() != '']

print(text_list)


"""
Given below list of words, identify the words that begin and end with the same character.
civic
trust
widows
maximum
museums
aa
as
"""
words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']

matching_words = [word for word in words if word[0] == word[-1]]

print("Words that begin and end with the same character:")
print(matching_words)