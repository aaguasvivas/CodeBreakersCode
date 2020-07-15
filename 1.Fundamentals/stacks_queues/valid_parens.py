def validParens(s):
    # O(n) time and space
    parens = ['(', ')', '[', ']', '{', '}']
    stack = []

    for c in s:
        idx = parens.index(c)
        if idx % 2 == 0:
            stack += c
        else:
            if len(stack) == 0:
                return False
            else:
                val = stack.pop()
                if val != parens[idx - 1]:
                    return False
    if not stack:
        return True
    else:
        return False


def balanced_parens(exp):
    closing = ['}', ')', ']']
    stack = []

    for character in exp:
        if character in closing:
            if len(stack) == 0:
                return False
            topElement = stack.pop()
            if character is '}' and topElement is not '{':
                return False
            if character is ')' and topElement is not '(':
                return False
            if character is ']' and topElement is not '[':
                return False
        else:
            stack.append(character)
    if len(stack) == 0 is False:
        return False
    return True


s = "()"
print(validParens(s))

s = "()[]{}"
print(validParens(s))

s = "(]"
print(validParens(s))

s = "([)]"
print(validParens(s))

s = "{[]}"
print(validParens(s))
