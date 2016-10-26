def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    bracket_stack = list()
    for i in range(len(s)):
        if s[i] == '{' or s[i] == '[' or s[i] == '(':
            bracket_stack.append(s[i])
        else:
            if len(bracket_stack) == 0:
                return False
            open_bracket = bracket_stack.pop()
            if open_bracket == '{' and s[i] != '}':
                return False
            if open_bracket == '[' and s[i] != ']':
                return False
            if open_bracket == '(' and s[i] != ')':
                return False
    if len(bracket_stack) != 0:
        return False
    return True


if __name__ == '__main__':
    print(isValid("()"))
