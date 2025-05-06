
def floor(ls, f):
    f += 1
    sum = 0
    for i in ls:
        if isinstance(i,(int, float)):
            sum += f
        elif isinstance(i, list):
            sum += floor(i, f)
    return sum

ls = eval(input())
print(floor(ls, 0))
