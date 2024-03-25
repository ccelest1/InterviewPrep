"""
Valid condition: string has all chars occurring at same frequency throughout or for a given string all chars will occur at same frequency if 1 is taken out
Given string s determine if valid, if so -> 'YES' else 'NO'
"""


def isValid(s):
    tracker = {}
    for char in s:
        tracker[char] = 1 + tracker.get(char, 0)
    # brute force
    unique = list(tracker.values())
    tracker2 = {}
    for val in unique:
        tracker2[val] = 1 + tracker2.get(val, 0)
    unique = list(tracker2.values())
    max_val = max(unique)


print(isValid("aabcdefghhgfedecba"))
