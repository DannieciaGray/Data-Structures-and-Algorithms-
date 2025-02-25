def checkBalancedParenthesis(s):
    # 1. Check if the string is empty. If so, raise a TypeError.
    if s == "":
        raise TypeError  # Must raise TypeError without arguments

    # 2. Create a stack to track opening brackets.
    stack = []
    matches = {")": "(", "}": "{", "]": "["}  # Mapping of closing to opening brackets

    # 3. Iterate through the string:
    for char in s:
        # If the current character is an opening bracket, push it onto the stack.
        if char in "({[":
            stack.append(char)
        # If it is a closing bracket:
        elif char in ")}]":
            # If the stack is empty, return "Unbalanced" (there's nothing to match it).
            if not stack:
                return "Unbalanced"
            # Otherwise, pop from the stack and check if it matches the expected opening bracket.
            top = stack.pop()
            if top != matches[char]:
                return "Unbalanced"

    # 4. If the stack is empty, return "Balanced"; otherwise, return "Unbalanced".
    return "Balanced" if not stack else "Unbalanced"


def getUnbalancedPositions(s):
    # 1. Check if the string is empty. If so, raise a TypeError.
    if s == "":
        raise TypeError  # Must raise TypeError without arguments

    # 2. Create a stack that stores tuples (opening bracket, index).
    stack = []
    matches = {")": "(", "}": "{", "]": "["}  # Mapping of closing to opening brackets

    # 3. Create a list to store indices of unbalanced brackets.
    unbalanced_indices = []

    # 4. Iterate through the string:
    for i, char in enumerate(s):
        # If the current character is an opening bracket, push (character, index) onto the stack.
        if char in "({[":
            stack.append((char, i))
        # If it is a closing bracket:
        elif char in ")}]":
            # If the stack is empty, it means this closing bracket has no match.
            if not stack:
                unbalanced_indices.append(i)
            else:
                # Pop the last opening bracket from the stack.
                top = stack.pop()
                if top[0] != matches[char]:  # Compare only the bracket (not the index)
                    unbalanced_indices.append(top[1])  # Mismatched opening bracket
                    unbalanced_indices.append(i)  # Mismatched closing bracket

    # 5. Any remaining unmatched opening brackets in the stack are also unbalanced.
    while stack:
        unbalanced_indices.append


