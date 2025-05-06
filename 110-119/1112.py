
#a = list(map(float, input().strip('[]').split(',')))
#b = list(map(float, input().strip('[]').split(',')))
a = list(map(float, input()[1:-1].split(",")))
b = list(map(float, input()[1:-1].split(",")))
print(a)

if len(a) != len(b):
    print("The length is not same")
else:
    mul = mo_a = mo_b = 0
    for i in range(len(a)):
        mul += a[i]*b[i]
        mo_a += a[i]**2
        mo_b += b[i]**2
    if mo_a == 0 and mo_b == 0:
        print("{:.6f}".format(1))
    elif mo_a == 0 or mo_b == 0:
        print("{:.6f}".format(0))
    else:
        ans = mul / (pow(mo_a, 0.5) * pow(mo_b, 0.5))
        print("{:.6f}".format(ans))



