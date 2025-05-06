def is_char(s):
    if ord("A")<=ord(s)<=ord("Z") or ord("a")<=ord(s)<ord("z"):
        return True
    return False

str = input()
x = int(input())
for i in str:
    if ord("A")<=ord(i)<=ord("Z"):
        print("{:c}".format((ord(i) - ord("A") + x) % 26 + ord("A")), end = '')
    elif ord("a")<=ord(i)<=ord("z"):
        print("{:c}".format((ord(i) - ord("a") + x) % 26 + ord("a")), end = '')
    else:
        print(i, end = '')
