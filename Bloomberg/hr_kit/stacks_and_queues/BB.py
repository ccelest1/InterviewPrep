def isBalanced(s: str) -> str:
    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []
    for bracket in s:
        print(stack)
        if bracket in pairs.keys():
            stack.append(bracket)
        else:
            if stack:
                if bracket == pairs[stack[-1]]:
                    stack.pop()
                else:
                    return "NO"
    if not stack:
        return "YES"


print(isBalanced("{[()]}"))
