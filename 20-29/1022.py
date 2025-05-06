
stopword = ''
str = ''
try:
    for line in iter(input, stopword):
        str += line + '\n'
except EOFError:
    pass

for i in str:

    if i == ',':
        print('\t', end = '')
    elif i == '\n':
        print('\t\n' ,end = '')
    else:
        print(i, end = '')

"""
import re

def replace_commas_with_tabs(input_lines):
    output_lines = []
    for line in input_lines:
        # 使用正则表达式将逗号替换为制表符
        new_line = re.sub(r',', '\t', line)
        output_lines.append(new_line)
    return output_lines

# 示例输入
input_data = [
    "city, a, b, c",
    "bj, 1, 2, 3",
    "xa, 2, 3, 4",
    "gz, 3, 4, 5",
    "cq, 1, 2, 2"
]

# 调用函数进行替换
output_data = replace_commas_with_tabs(input_data)

# 打印输出结果
for line in output_data:
    print(line)

"""