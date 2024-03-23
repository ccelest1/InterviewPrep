"""
- Repeated string

Given string s, repeated infinite times -> return number of letter a's occurring in first n letters of infinite string

* ex:
    input: s(str) - 'abcac', n(int) - 10
    output: int - 4
"""


def repeatedString(s: str, n: int) -> int:
    def helper(string):
        a_occ = 0
        for i in range(len(string)):
            if string[i] == "a":
                a_occ += 1
        return a_occ

    repeated = (n // len(s)) * helper(s)
    remainder = n % len(s)

    # missing this part
    a_occ_remainder = helper(s[:remainder])

    return repeated + a_occ_remainder


print(repeatedString("a", 1000000000000))
print(repeatedString("gfcaaaecbg", 547692))
print(repeatedString("aba", 10))
