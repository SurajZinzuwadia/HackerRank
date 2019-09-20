def solve(s):
    name = s.split(' ')
    return ' '.join((word.capitalize() for word in name))
