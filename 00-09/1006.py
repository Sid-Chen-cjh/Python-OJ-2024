"""
题目描述
回文串的判断
回文串的定义是反向排列与原串相同。

输入
一行一个字符串，表示提供给你的字符串。

输出
输出 'True' 表示输入的串是回文串；否则输出 'False' 。

样例输入
25252

样例输出
True
"""
a = input()

if a == a[::-1]:
    print("True")
else:
    print("False")

"""
a[start:stop:step]
start：起始索引，默认为 0。
stop：结束索引，默认为序列的长度。
step：步长，默认为 1。
"""