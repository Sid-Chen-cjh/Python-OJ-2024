amount = input()
last = amount[-1]
num = int(amount[:-1])
if last == 'R' or last == 'r':
    ans = int( num / 6 )
    print(f"{ans}D")
elif last == 'D' or last == 'd':
    ans = num * 6
    print(f"{ans}R")
else:
    print("Error!")

"""
first_char = input_str[0]  # 获取第一个字符
second_char = input_str[1]  # 获取第二个字符
last_char = input_str[-1]  # 获取最后一个字符
second_last_char = input_str[-2]  # 获取倒数第二个字符
substring = input_str[1:4]  # 获取从索引 1 到 3 的子字符串
substring = input_str[2:]  # 获取从索引 2 开始到末尾的子字符串
substring = input_str[:3]  # 获取从开头到索引 2 的子字符串
"""
