"""
题目描述
字符串存在判定

输入
输入第一个字符串表示字符串 a；
第二行一个字符串 b

输出
输出 'True' 或者 'False' ，表示字符串是否存在。

样例输入
3
233

样例输出
True
"""
a = input()
b = input()

if b in a:
    print("True")
else:
    if a in b:
        print("True")
    else:
        print("False")

"""
in
"""