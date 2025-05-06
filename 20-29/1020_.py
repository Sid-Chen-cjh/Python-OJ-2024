#!/usr/bin/python3

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def eval(s):
    a = ''
    for i in s[6:-1]:
        a += i
        a = a.strip()
    b = a.split(',')
    c = 1
    for i in range(len(b)):
        if b[i].isdigit():
            c *= int(b[i])
        elif is_float(b[i]):
            c *= float(b[i])
        else:
            return 'Invalid arg '+str(i+1)
    return c

print(eval(input()))