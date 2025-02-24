# Arguments:
    # s (str): A string containing parentheses, brackets, and/or braces.

# Returns:
    # "Balanced" (str): If all parentheses, brackets, and braces are properly matched and nested.
    # "Unbalanced" (str): If the parentheses, brackets, or braces are not properly matched or nested.

# Errors Raised:
    # TypeError: If the input string is empty.
def checkBalancedParenthesis(s):
    # 1. Check if the string is empty. If so, raise a TypeError.
    if s == "":
        raise TypeError("Input string cannot be empty")

    # 2. Create a stack to track opening parentheses, brackets, or braces.
    stack = []
    matches = {")": "(", "}": "{", "]": "["}  # Mapping of closing to opening brackets
    # 3. Iterate through the string:
    for char in s:
        # If the current character is an opening bracket, push it onto the stack.
        if char in "{[(":
            stack.append(char)
        # If it is a closing bracket:
        if char in ")]}":
            # If the stack is empty, return "Unbalanced" (there's nothing to match it).
            if not stack:
                return "Unbalanced"
            #Otherwise, pop from the stack and check if it matches the expected opening bracket.
            top = stack.pop
            if top != matches[char]:
                return "Unbalanced"
            

    # 4. After iteration, if the stack is empty, return "Balanced".
    if not stack:
        return "Balanced"

    #Otherwise, return "Unbalanced" (indicating unmatched opening brackets).
    return "Unbalanced"


# Arguments:
    # s (str): A string containing parentheses, brackets, and/or braces.

# Returns:
    # list[int]: A sorted list of indices where unmatched/unbalanced parentheses, brackets, or braces occur.

# Errors Raised:
    # TypeError: If the input string is empty.
def getUnbalancedPositions(s):
    # Steps:
    # 1. Check if the string is empty. If so, raise a TypeError.
    if s == "":
        raise TypeError("Input string cannot be empty")

    # 2. Create a stack that stores tuples (opening bracket, index).
    # 3. Create a list to store indices of unbalanced closing brackets.
    # 4. Iterate through the string:
    #    - If the current character is an opening bracket, push (character, index) onto the stack.
    #    - If it is a closing bracket:
    #      - If the stack is empty, add its index to the unbalanced list (it has no match).
    #      - Otherwise, pop from the stack and check if it matches the expected opening bracket.
    # 5. After iteration, any remaining items in the stack are unmatched opening brackets, 
    #    so add their indices to the unbalanced list.
    # 6. Return the sorted list of unbalanced indices.

