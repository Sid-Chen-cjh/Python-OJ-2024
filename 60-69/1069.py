# 可能出错：
# Error:Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
# print("{}".format(pow(2, P) - 1))

import math as m
P = int(input())
d = m.ceil(P * m.log10(2))   #math.ceil 和 math.log10
ans = pow(2, P) - 1
t = pow(2, P) - 1
#  d = len(str(ans))
q = []
for i in range(10):
    temp = t % pow(10, 50)
    t //= pow(10, 50)
    q.append(temp)
q.reverse()

print(d)
for i in q:
    print("{:0>50}".format(i))
print(int(str(ans)[0]))

