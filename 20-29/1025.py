def sun(x):
    sum = 0
    for i in x:
        sum += i
    return sum
def ave(x):
    return sum(x)/len(x)

stopword = ''
num = []
try:
    for line in iter(input,stopword):
        num.append(float(line.strip()))
except EOFError:
    pass

a = []
for i in num:
    a.append(pow(i-ave(num),2))
ans = pow(sum(a)/(len(a)-1),0.5)

print("dev = {:.2}.".format(ans))
