# Validation: Checking if a string fits a particular format, such as validating emails or phone numbers.
# Data Extraction: Extracting useful data such as hashtags, email addresses, or phone numbers from raw text.
# Text Replacement: Replacing text, such as anonymizing user data.
# String Splitting: Breaking up text based on specific delimiters.
# Searching for Patterns: Finding occurrences of a particular pattern within a text.

# Literal Characters: These are characters that match exactly what they represent. For instance, the letter a will match the character 'a' in a string.
# Metacharacters: These are characters with special meanings in regex patterns. Some examples include:
#   .: Matches any character except a newline.
#   ^: Matches the start of a string.
#   $: Matches the end of a string.
#   []: Matches any one of the characters inside the brackets.
# Special Sequences: These are combinations of a backslash \ followed by a character that has special meaning. For example:
#   \d: Matches any digit (equivalent to [0-9]).
#   \w: Matches any word character (equivalent to [a-zA-Z0-9_]).
#   \s: Matches any whitespace character (spaces, tabs, line breaks).

import re

# re.findall(pattern, text)
text = "Hi my name is Travis, and I like to go and do things and stuff"
ands = re.findall(r"and", text)  #re.findall() returns a list of all occurrances of the given regex pattern within the text.
print(ands)  # Output: ['and', 'and', 'and'] 
print(len(ands))  # Output: 3 	Here we use the len() function to get the number of items in the list that was returned to us

tweets = [
    "Loving the #sunset! So peaceful #nature #blessed",
    "Had a great day! #happy #friends #goodvibes",
    "Can't wait for the #weekend! #fun #relax"
]

hash_tags = []
for text in tweets:
    hashs = re.findall(r"#\w+", text)
    hash_tags.extend(hashs)
print(hash_tags)



# re.search(pattern, text)
# The re.search() function searches through a string for the first occurrence of a pattern and returns a match object if a match is found.
# It only finds the first match, making it ideal for validation purposes, like checking if an email address is valid.
# If no match is found, it returns None.
email = "kareem33-34-28@gmail.com"
found = re.search(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email) # This will returns a match object
if found:
    print(f"{found.group()} is a valid email! Please click continue!")



# re.match(pattern, text)
# The re.match() function checks whether the beginning of a string matches a specified pattern.
# This method is different from re.search() because re.match() only checks the start of the string.
# If the pattern is found at the beginning, a match object is returned; otherwise, it returns None.
url = "https://something.com"
secure = re.match(r"https", url)
if secure:
    print("This link goes to a secure website!")  # Output: This link goes to a secure website!



# re.split(pattern, text)
text = 'Python,Regex;Splitting-Example. Fun, right!'
words = re.split(r"[,.;\s!-]+", text)
print(words)  



# re.sub(pattern, replacer, text)
number = "(770) 888-1180"
formatted_number = re.sub(r"\D", '', number) # r"\D" matches any character that is not a digit. \D is the inverse of \d, which matches digits.
print(formatted_number)  # Output: 7708881180

chat = '''
@Yve-bee123 : "I think I love Regex"
@Travis : "Aren't you married?"
@Yve_bee123 : "It's just not the same"
@Travis : "They better not see this!"
'''

anon_chat = re.sub(r"@[\w-]+", '@user-anon', chat)
print(anon_chat)



# Grouping with Regex <<<()>>>
# re.search(pattern, text).group(n)
text = "123-456"
pattern = r"(\d+)-(\d+)"
thematch = re.search(pattern, text)
if thematch:
    print(f"Group  : {thematch.group()}")  # Output: 123-456
    print(f"Group 0: {thematch.group(0)}")  # Output: 123-456
    print(f"Group 1: {thematch.group(1)}")  # Output: 123
    print(f"Group 2: {thematch.group(2)}")  # Output: 456
