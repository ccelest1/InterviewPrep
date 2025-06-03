# 02.29.24
"""
Pangrams - string containing every character in alphabet
Given a sentence determine if it's a pangram
ignore case
return either pangram, not pangram as appropriate
"""

"""
create an array with 26 subarrays (corresponding to each char in alphabet)
"""


class Solution:
    def pangrams(s):
        for i in range(97, 122, 1):
            if chr(i) not in s.lower():
                return "not pangram"
        return "pangram"


s = "The quick brown fox jumps over the lazy dog"
# print(Solution.pangrams(s) == "pangram")
# s = "The"
# print(Solution.pangrams(s) == "not pangram")

"""
determine if string is funny or not
create a copy of string in reverse and iterate through string and compare abs differences in ascii values of chars
"""


class Solution2:
    def is_funny(s):
        if not s:
            return
        rev = s[::-1]
        for i in range(1, len(s)):
            if (abs(ord(s[i]) - ord(s[i - 1]))) != abs((ord(rev[i])) - ord(rev[i - 1])):
                return "Not Funny"
        return "Funny"


# print(Solution2.is_funny("lmnop"))

"""
Alternating Chars
Given a string containing chars A, B only. Task = change to string so there are no matching adjacent chars
Allowed to delete 0 or more chars in string

Task: find min # of required deletions
"""


def alternatingCharacters(s: str) -> int:
    if not s:
        return 0
    current_char = s[0]
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == current_char:
            deletions += 1
        else:
            current_char = s[i]
            continue
    return deletions


print(alternatingCharacters("AAAA"))
print(alternatingCharacters("AAABBB"))
