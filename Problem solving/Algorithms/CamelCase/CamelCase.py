# Complete the camelcase function below.
def camelcase(s):
    result = 0
    for i in range(0,len(s)):
        if(s[i].isupper()):
            result+=1
    return (result + 1)
if __name__ == '__main__':
    s = input()

    result = camelcase(s)
    print(result)