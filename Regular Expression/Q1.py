

import re
from typing import Pattern

# # 1. Write a Python program to check that a string contains only a certain 
# #     set of characters (in this case a-z, A-Z and 0-9).
# def Check(string):
#     char = re.compile(r"[^a-zA-Z0-9.]")
#     if not char.search(string):
#         print("True")
#     else:
#         print("False")
# Check("Arko123Dibyendu")
# Check("ABCDEFabcdef123450")
# Check("&%@#!}{a123")


# # 2. Write a Python program that matches a string that has an a followed by zero or more b's.
# def Matches(txt):
#     Patterns = 'ab*?'
#     if re.search(Patterns, txt):
#         print("Find the match")
#     else:
#         print("Not Find the match")

# Matches("abcd")
# Matches("ac")
# Matches("dffc")
# Matches("Dibyendu")
# Matches("ok ji")


# # 3. Write a Python program that matches a string that has an a followed by one or more b's.
# def Matches(txt):
#     Patterns = 'ab+?'
#     if re.search(Patterns, txt):
#         print("Find the match")
#     else:
#         print("Not Find the match")

# Matches("abcd")
# Matches("ac")
# Matches("dffc")
# Matches("Dibyendu")
# Matches("ok ji")


# # 4. Write a Python program that matches a string that has an a followed by zero or one 'b'
# def Matches(txt):
#     Patterns = 'ab?'
#     if re.search(Patterns, txt):
#         print("Find the match")
#     else:
#         print("Not Find the match")

# Matches("abcd")
# Matches("ac")
# Matches("dffc")
# Matches("dibyendu")
# Matches("ok ji")


# # 5. Write a Python program to find sequences of lowercase letters joined with a underscore.
# def text_match(text):
#         patterns = '^[a-z]+_[a-z]+$'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
# print(text_match("aab_cbbbc"))
# print(text_match("aab_Abbbc"))
# print(text_match("Aaab_abbbc"))


# # 6. Write a Python program to remove leading zeros from an IP address.
# ip = "216.08.094.196"
# string = re.sub('\.[0]*', '.', ip)
# print(string)


 