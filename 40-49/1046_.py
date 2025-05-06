"""
import math

a = list(map(int, input().split('/')))
b = list(map(int, input().split('/')))
son = a[0]*b[1] + a[1]*b[0]
mthr = a[1]*b[1]
temp = math.gcd(son, mthr)
son //= temp
mthr //= temp
if son == 0:
    print("0/1")
elif son/mthr < 0:
    print("-{}/{}".format(abs(son), abs(mthr)))
else:
    print("{}/{}".format(son, mthr))
"""
import fractions

a = list(map(int, input().split('/')))
b = list(map(int, input().split('/')))
a = fractions.Fraction(a[0], a[1])
b = fractions.Fraction(b[0], b[1])
ans = a+b
ans = fractions.Fraction(ans)
if ans.numerator == 0:
    print("0/1")
else:
    print(ans)

# class fractions.Fraction(numerator=0, denominator=1)
# class fractions.Fraction(int|float|str|Decimal|Fraction)