
stopword = ''
l = 0
str = []
try:
    for line in iter(input, stopword):
        str.append(line)
        l += 1
        if l == 6:
            break
except EOFError:
    pass

in_str = {}
for i in range(l//2):
    in_str[str[2*i]] = str[2*i+1]

if "Pile" in in_str and in_str["Pile"] == "MAKIKAWAYI":
    print("SUCCESS")
else:
    print("FAILED")