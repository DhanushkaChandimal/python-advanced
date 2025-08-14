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