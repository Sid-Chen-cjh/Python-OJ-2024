a = int(input())
if a < 0:
    print('-',end = '')
print("0x{:x}".format(abs(a)))