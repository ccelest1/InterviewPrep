"""
sherlock - considers str to be valid if all chars of str appear same # of times or if one can remove just 1 char @ 1 index in string and all chars occur at same # of times
if string is valid, return 'YES' else 'NO'
"""


def isValid(s):
    tracker = {}
    for char in s:
        tracker[char] = 1 + tracker.get(char, 0)
    # brute force
    freq = {}
    for value in tracker.values():
        freq[value] = 1 + freq.get(value, 0)
    if len(freq) == 1:
        return "YES"
    if len(freq) > 2:
        return "NO"

    max_freq = max(list(freq.values()))

    for key in freq.keys():
        print(key)
        if freq[key] == max_freq:
            max_key = key
    for key in freq.keys():
        if freq[key] != max_freq:
            if freq[key] > 1:
                return "NO"
            if key - 1 == max_key or key - 1 == 0:
                return "YES"
    return "NO"


def isValid_simple(s):
    tracker = {}
    for char in s:
        tracker[char] = 1 + tracker.get(char, 0)
    freq = {}
    for value in tracker.values():
        freq[value] = 1 + freq.get(value, 0)
    print(freq)
    if len(freq) == 1:
        return "YES"
    if len(freq) > 2:
        return "NO"

    max_freq = max(freq)
    min_freq = min(freq)

    if freq[max_freq] == 1 and (max_freq - min_freq == 1 or max_freq == 1):
        return "YES"

    if freq[min_freq] == 1 and min_freq == 1:
        return "YES"

    return "NO"


# print(isValid("abc"))
# print(isValid("abcc"))
# print(isValid("abccc"))
# print(isValid("abbac"))
# print(isValid("aabbcd"))
print(isValid_simple("aabbccddeefghi"))
print(isValid_simple("abcdefghhgfedecba"))
print(isValid_simple("aaaaabc"))

"""
    else:
        for i in range(1, len(unique)):
            print(unique[i])
            if (
                unique[i] != unique[0]
                and unique[i] - 1 == unique[0]
                and i == len(unique) - 1
                and unique[i - 1] == unique[0]
            ):
                return "YES"
            elif i == len(unique) - 1 and unique[i] == unique[0]:
                return "YES"
            elif (
                i == len(unique) - 1
                and unique[i] - 1 == 0
                and unique[i - 1] == unique[0]
            ):
                return "YES"
    return "NO"

"""
