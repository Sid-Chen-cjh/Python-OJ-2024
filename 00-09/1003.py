"""
题目描述
eval() 函数的使用

输入
输入一行一个字符串，表示 eval() 函数所需要执行的语句。保证可以正常执行 eval() 函数。

输出
输出 eval() 函数执行的语句。

样例输入
print('hello')

样例输出
hello

提示
程序输入有print()函数了 考虑一下输出时候是否还需要使用print() 函数.
"""
# 读取输入
input_str = input()

# 执行 eval() 函数
eval(input_str)

"""
笔记：
eval() 函数可以将字符串转化为 Python 表达式，并执行。
"""