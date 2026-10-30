# import re
#
# pattern = ["samba", "f50"]
# text = "I will be the boot: f50, you selected to over to your new location by Evening"
#
# for pattern in pattern:
#     print("I am searching for "+ pattern)
#
#     if re.search(pattern, text):
#         print("Match!!!")
#     else:
#         print("No Match!")

import re

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for patterns {}".format(pat))
        print(re.findall(pat, phrase))
        print("\n")


text_phrase = 'This is a string! it has punctuation. how can we remove it?'
text_pattern = ['[^!.?]+']

multi_re_find(text_pattern, text_phrase)
