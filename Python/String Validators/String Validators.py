if __name__ == '__main__':
    s = input()
    a=any(s1.isalnum() for s1 in s)
    b=any(s1.isalpha() for s1 in s)
    c=any(s1.isdigit() for s1 in s)
    d=any(s1.islower() for s1 in s)
    e=any(s1.isupper() for s1 in s)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
