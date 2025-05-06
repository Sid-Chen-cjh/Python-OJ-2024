n = int(input())
call = []
for i in range(n):
    call.append(input())
for i in call:
    if len(i) != 11:
        print("Halation - I can't join it!")
    else:
        print("6{}".format(i[-5:]))
