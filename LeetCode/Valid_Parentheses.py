def ValidParentheses(s):
    stack = []
    for b in s:
        if b in "({[":
            stack.append(b)
        elif b in ")}]":
            if not stack:  # Check if stack is empty
                return False
            
            if stack[-1] == "(" and b == ")":
                stack.pop()
            elif stack[-1] == "{" and b == "}":
                stack.pop()
            elif stack[-1] == "[" and b == "]":
                stack.pop()
            else:
                return False  # Mismatched bracket
    
    # If stack is empty, parentheses are valid
    return not stack

# Test cases
print(ValidParentheses("()"))        # True
print(ValidParentheses("()[]{}"))    # True
print(ValidParentheses("(]"))        # False
print(ValidParentheses("([)]"))      # False
print(ValidParentheses("{[]}"))      # True
print(ValidParentheses("})]}"))      # False
