import json

def h_index(ls):
    ls.sort()
    ans = []
    for i in range(len(ls)):
        ans.append(min(ls[i], len(ls)-i))
    return max(ans)

n = int(input())
a = []
for i in range(n):
    a.append(json.loads(input()))
#自查：
# print(json.dumps(a, indent = 4))
# print("==========================================")
author = {}
#论文数；引用数；至少引用5次论文数
for i in a:
    for j in i["authors"]["authors"]:
        temp = j["full_name"]
        if temp not in author:
            author[temp] = []
    if i["citing_paper_count"] >= 1:
        for t in i["authors"]["authors"]:
            author[t["full_name"]].append(i["citing_paper_count"])
# print(author)
H = {}
h = []
for i in author:
    H[i] = h_index(author[i])
    if H[i] not in h:
        h.append(H[i])
        h.sort(reverse=True)

# 根据字典的值逆序排列的一种用法，返回的是由元组组成的列表，不完全符合题意是因为没有按key再排序
# H = sorted(H.items(), key = lambda x:x[1], reverse = True)
"""
# 一种更美的sorted()排序方法
sorted_dict = dict(sorted(H.items(), key=lambda item: (-item[1], item[0])))
print(sorted_dict)
========================================
lambda: 这是 Python 的一种创建匿名函数的方式。
        匿名函数是指没有通过 def 语句正式定义名称的函数。
        lambda 表达式可以接受任意多个参数，但只能有一个表达式，
        它的语法如下：
lambda 参数1, 参数2, ... : 表达式
lambda 表达式的主体是一个单一的表达式而不是代码块。
        表达式的值就是这个匿名函数的返回值。
========================================
"""
for i in h:
    temp = []
    for j in H:
        if H[j] == i:
            temp.append(j)
    temp = sorted(temp)
    for t in temp:
        print(t, end = ' ')
        print(i)
