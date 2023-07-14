from structure.array.ArrayStack import ArrayStack


def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise"""
    lefty = '({['  # opening delimiters
    righty = ')}]'
    s = ArrayStack.ArrayStack()
    for c in expr:
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.is_empty():
                return False
            if righty.index(c) != lefty.index(s.pop()):
                return False
    return s.is_empty()


def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise."""
    S = ArrayStack.ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j + 1)
        if k == -1:
            return False
        tag = raw[j + 1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k + 1)  # find next '<' character (if any)
    return S.is_empty()


s = "<a></a><c><b></b></c>"
print(is_matched_html(s))
