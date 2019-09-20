def mutate_string(string, position, character):
    l = list(string)
    l[position] = str(character)
    string = ''.join(l)
    return string

