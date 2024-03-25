"""
Given two strings, determine if they share a common substr
substr may be as small as 1 char
    ex:
        (1) 'and','art' shares 'a' -> (2) 'be', 'cat' shares nothing

    return 'YES', 'NO' depending on if they share common char
"""


def twoStrings(s1, s2):
    if not s1 or not s2:
        return
    s1_map = {}
    for char in s1:
        s1_map[char] = 1 + s1_map.get(char, 0)
    for char in s2:
        if char in s1_map:
            return "YES"
    return "NO"
