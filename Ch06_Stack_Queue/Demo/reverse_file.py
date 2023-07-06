from ArrayStack import ArrayStack


def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    # now we overwrite with contenes in LIFO order
    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()


if __name__ == '__main__':
    reverse_file('reverseFile.txt')
