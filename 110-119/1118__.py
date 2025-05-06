#!/usr/bin/python3
# answer
def function(lst,k,rank):
    cnt = 0
    for i in lst:
        if rank != k and isinstance(i,list):    #如果当前层数不是指定层数，并且该元素为列表，那么我们就进入该列表，然后增加一个层数
            cnt += function(i,k,rank+1)
        elif rank == k and isinstance(i,int) or isinstance(i,float):   #如果是当前层数，并且是数字，就加起来
            cnt += 1
    return cnt
# isinstance 是 Python 内置函数，
# 用于判断一个对象是否是指定类型或类型的元组中的任意一个。
# isinstance(object, classinfo)
# object: 需要检查的对象。
# classinfo: 类型或类型组成的元组。
#            如果是一个元组，则只要对象是其中任何一个类型的实例就会返回 True。
ls = eval(input())
k = int(input())
print(function(ls,k,1))               #函数（列表，指定层数，从第一层开始）



"""
# 递归的正确操作。这里也可以用global全局变量
# 但考虑到全局变量在递归中会出现反复声明和调用,所以用恒定的局部变量效果相差不大
def search(ls, m, t, ans):
    t += 1
    for i in ls:
        if t == m and str(i).isdigit():
            ans += 1
        if not str(i).isdigit():
            ans = search(eval(str(i)), m, t, ans)
    return ans

a = eval(input())
b = int(input())
print(search(a, b, 0,0))
"""