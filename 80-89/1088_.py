def dimension_reduction(ls, ans):
    for i in ls:
        if isinstance(i, (int, float)):
            ans.append(i)
        else:
            dimension_reduction(i, ans)

p = []
stopword = ''
try:
    for line in iter(input, stopword):
        ans = []
        dimension_reduction(eval(line), ans)
        p.append(ans)
except:
    pass
for i in p:
    print(i)
"""
from collections.abc import Iterable

def flatten_deep(lst):
    for i in lst:
        if isinstance(i, Iterable) and not isinstance(i, (str, bytes)):
            yield from flatten_deep(i)
        else:
            yield i

# 示例用法
nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
flattened_list = list(flatten_deep(nested_list))
print(flattened_list)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8]

"""
"""
提供的代码片段是用于将嵌套的列表展平（flatten）的。
flatten_deep函数使用了yield from来递归地展平列表。这个方法非常简洁且高效。
以下是对你提供的flatten_deep函数的解释：
flatten_deep函数：这个函数接受一个列表lst作为参数。
for i in lst：遍历列表中的每个元素。
if isinstance(i, Iterable)：检查当前元素是否是一个可迭代对象（如列表、元组等）。
yield from flatten_deep(i)：如果元素是可迭代对象，则递归调用flatten_deep函数，并将结果逐个yield出来。
else：如果元素不是可迭代对象，则直接yield该元素。
这个函数会生成一个展平的列表中的所有元素，可以使用列表推导式或list()函数将其转换为列表。
注意：在检查是否为可迭代对象时，排除了str和bytes，因为它们在某些情况下也被认为是可迭代的，但通常我们不希望将字符串或字节展平为单个字符。
"""