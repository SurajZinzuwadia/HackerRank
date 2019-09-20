def formatted_String(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(' '.join(map(lambda x: x.rjust(width), [str(i), oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]])))
